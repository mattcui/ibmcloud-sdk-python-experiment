import json
from client import Session
from ibm_platform_services.global_search_v2 import GlobalSearchV2

def query():
	global_search_v2 = Session().client()
	response = global_search_v2.search(
			query='type:volume AND family:is',
			fields=['*'],
			limit=10)
	scan_result = response.get_result()

	print(json.dumps(scan_result, indent=2))