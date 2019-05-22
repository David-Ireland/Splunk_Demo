




# How to Index HTTP events in Splunk


## Configure the Splunk instance to index events

Select 'Settings' > 'Add Data'

<img width="600px" src="screenshots/screenshot1.png">


Select 'Monitor'

<img width="600px" src="screenshots/screenshot2.png">

Select 'HTTP Event Collector' > Add a Source Name > Select 'Next'

<img width="600px" src="screenshots/screenshot3.png">

Select 'Create a new index'

Add a index name and set size to 10MB and select 'Save'

Add the new index to 'Allowed Indexes' and select it from the dropdown

Select 'Review' then 'Done'

<img width="600px" src="screenshots/screenshot4.png">

Copy the 'Token Value'

<img width="600px" src="screenshots/screenshot5.png">


## Configure the Splunk index settings

Select 'Settings' > 'Data inputs' > 'HTTP Event Collector' > 'Global Settings'

Enable all tokens

Uncheck SSL

Make sure HTTP port number is 8088

<img width="600px" src="screenshots/screenshot6.png">





Create a Python script 