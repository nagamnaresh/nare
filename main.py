import requests
import json
# from pprint import pprint

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    res = requests.get('https://api.covid19india.org/state_district_wise.json')
    # s3.put_object(Bucket ="s3-covid-details", key = "covid_details.json", body = str(res))
    for i in res:
        print("active:",i["active"])
    return {
        'statuscode':200,
        'body':josn.dump('hello naresh')
    }