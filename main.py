import os
import requests
from lib.json_file_write import json_file_write

asset_search_url = "https://api.criminalip.io/v1/asset/search"
get_asset_report_url = "https://api.criminalip.io/v1/asset/ip/report"
domain_scan_url = "https://api.criminalip.io/v1/domain/scan"
get_domain_report_url = "https://api.criminalip.io/v2/domain/report/"
criminal_ip_api_key = os.environ.get("CRIMINAL_IP_API_KEY","")
search_value = ""
search_type = input("어떤 API를 호출할지 선택하세요.\n1. Asset Search\n2. Get Asset Search Report\n3. Domain Scan\n4. Get Domain Scan Report\n: ")

def call_crimial_ip_api (criminal_ip_api_key:str, search_value:str):
    """Call Criminal IP API

    Args:
        criminal_ip_api_key (str): criminal ip api key
        search_value (str): asset search api search value
    """
    try:
        search_value = input("검색할 자산 정보를 입력하세요\nasset search, asset report 조회는 ip 입력\ndomain scan은 url입력\ndomain scan report 조회는 scan id 입력\n: ")
        url_with_qs = ""
        filename = ""
        req_body = ""
        if search_type == "1":
            url_with_qs = f"{asset_search_url}?query={search_value}&offset=0"
            filename = "asset_search"
        elif search_type == "2":
            url_with_qs = f"{get_asset_report_url}?ip={search_value}&full=true"
            filename = "asset_report"
        elif search_type == "3":
            url_with_qs = domain_scan_url
            filename = "domain_scan"
            req_body = {"query": search_value}
        elif search_type == "4":
            url_with_qs = f"{get_domain_report_url}/{search_value}"
            filename = "domain report"
        res = requests.get(url_with_qs, headers={"x-api-key": criminal_ip_api_key})
        if req_body:
            res = requests.post(url_with_qs, headers={"x-api-key": criminal_ip_api_key}, data=req_body)        
        res_json = res.json()["data"] if res.json().get("data") else res.json()
        json_file_write(filename, res_json)
    except Exception as e:
        print(f"asset search fail: {e}")

if __name__ == "__main__":
    call_crimial_ip_api(criminal_ip_api_key, search_value)
