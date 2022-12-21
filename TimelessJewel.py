#!/bin/python3
import argparse
import json

Sample = "sample.json"
Jewels_Name = ["致命的驕傲"]
Jewels_Type = ["永恆珠寶"]
Generals = {
    "致命的驕傲": ["kaom", "rakiata", "akoya"]
}
General_option_str = "explicit.pseudo_timeless_jewel_"
Html_API = "https://web.poe.garena.tw/trade/search/?q="

def get_json():
    with open (Sample, 'r') as json_file:
        query = json.load(json_file)
        return query

def get_query_json(query_json):

    query_json["name"] = Jewels_Name[0]
    query_json["type"] = Jewels_Type[0]

    for i in range(0, len(args.numbers)):

        general = "kaom"
        jewel_filter = dict()
        jewel_filter["id"] = "%s%s" % (General_option_str, general)
        jewel_filter["disabled"] = False
        jewel_filter["value"] = {
            "min": args.numbers[i],
            "max": args.numbers[i]
        }
        query_json["stats"][0]["filters"].append(jewel_filter)

    return query_json

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='')

    parser.add_argument(
        '-n',
        '--numbers',
        nargs='+',
        required=True,
        help="Input list of numbers.")

    args = parser.parse_args()

    query = get_json()
    get_query_json(query["query"])

    with open ("output", 'w') as json_file:
        json_file.write(Html_API)
        json.dump(query, json_file, ensure_ascii=False, indent=4)

