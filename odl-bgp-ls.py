import urllib
import json
import re

#url = raw_input ('Enter URL: ')

url = 'http://10.62.60.51:8181/restconf/operational/network-topology:network-topology'

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

js = json.loads(str(data))

#js = json.dumps(data)

#js = json.loads(data)


#print js
for item in js['network-topology']['topology']:
    print 'Topolgy Ids: ', item['topology-id']

print js['network-topology']['topology'][3]['node'][0]['l3-unicast-igp-topology:igp-node-attributes']['prefix']
print re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)', js['network-topology']['topology'][3]['node'][0]['termination-point'][0]['tp-id'])

print js['network-topology']['topology'][3]['node'][1]['l3-unicast-igp-topology:igp-node-attributes']['prefix']
print re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)', js['network-topology']['topology'][3]['node'][1]['termination-point'][0]['tp-id'])

print 'Link 1 Source: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)' ,js['network-topology']['topology'][3]['link'][0]['source']['source-tp'])
print 'Link 1 Destination: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)' ,js['network-topology']['topology'][3]['link'][0]['destination']['dest-tp'])
print 'Link 2 Source: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)' ,js['network-topology']['topology'][3]['link'][1]['source']['source-tp'])
print 'Link 2 Destination: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)' ,js['network-topology']['topology'][3]['link'][1]['destination']['dest-tp'])
print 'Link 3 Source: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)' ,js['network-topology']['topology'][3]['link'][2]['source']['source-tp'])
print 'Link 3 Destination: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)' ,js['network-topology']['topology'][3]['link'][2]['destination']['dest-tp'])
print 'Link 4 Source: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)' ,js['network-topology']['topology'][3]['link'][3]['source']['source-tp'])
print 'Link 4 Destination: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)' ,js['network-topology']['topology'][3]['link'][3]['destination']['dest-tp'])

#for item in js['comments']:
#    print 'Name: ', item['name']
#    print 'Count: ', item['count']
