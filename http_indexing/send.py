
import requests



# token = '211a0e6d-25ac-45ce-8f4c-66192ae360a2'

# curl -k http://bigdecision:8088/services/collector -H 'Authorization: Splunk 211a0e6d-25ac-45ce-8f4c-66192ae360a2' -d '{"event":"Hello from the event collector"}'





# curl -k http://localhost:8088/services/collector -H 'Authorization: Splunk 9a78a566-e388-46be-9811-ceed0a2904e6' -d '{"event":"Hello from the event collector"}'

# Localhost
token = '9a78a566-e388-46be-9811-ceed0a2904e6'

port = '8088'

uri = 'http://localhost:' + port + '/services/collector'

header = {'Authorization': 'Splunk ' + token} 

payload = '{"event": {"String Test" : "This is from a python script"} }'


print(requests.post(uri, data=payload, headers=header).text)
