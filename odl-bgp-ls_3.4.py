import urllib.request
import json
import re
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# url = raw_input ('Enter URL: ')

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

url = 'http://10.62.60.51:8181/restconf/operational/network-topology:network-topology'

password_mgr.add_password(None, url, 'admin', 'admin')

print('Retrieving', url)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)

uh = urllib.request.urlopen(url)
data = uh.read().decode("utf-8")
print('Retrieved', len(data), 'characters')

# js = json.dumps(data)

js = json.loads(data)

# print(js)


for item in js['network-topology']['topology']:
    print('Topology ID: ', item['topology-id'])

# print js
for item in js['network-topology']['topology']:
    if 'example-linkstate-topology' in item['topology-id']:
        if 'node' in item:
            print('Topology ID: ', item['topology-id'])
            print('Node Content:', item['node'])

            for i in item['node']:
#                print (i['l3-unicast-igp-topology:igp-node-attributes'])
                print ('Node ID: ', i['node-id'])
#                print (i['termination-point'])

        if 'link' in item:
#           print('Topology ID: ', item['topology-id'])
#           print('Link Content:', item['link'])

            for i in item['link']:
#                s = re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)', i['source']['source-tp'])
#                d = re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)', i['destination']['dest-tp'])
                snode = re.findall('router=(.+)', i['source']['source-node'])
                dnode = re.findall('router=(.+)', i['destination']['dest-node'])
                G.add_nodes_from(snode)
                G.add_nodes_from(dnode)
                G.add_edge(snode[0],dnode[0])
 #               print('Snode: ', snode)
 #               print('Dnode: ', dnode)
                print (snode[0], dnode[0])

nx.draw(G)
plt.show()


#    print('Empty Topology Ids: ', item['topology-id'])

# print(js['network-topology']['topology'][3]['node'][0]['l3-unicast-igp-topology:igp-node-attributes']['prefix'])
# print(re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                 js['network-topology']['topology'][3]['node'][0]['termination-point'][0]['tp-id']))

# print(js['network-topology']['topology'][3]['node'][1]['l3-unicast-igp-topology:igp-node-attributes']['prefix'])
# print(re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                js['network-topology']['topology'][3]['node'][1]['termination-point'][0]['tp-id']))

# print('Link 1 Source: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                                    js['network-topology']['topology'][3]['link'][0]['source']['source-tp']))
# print('Link 1 Destination: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                                         js['network-topology']['topology'][3]['link'][0]['destination']['dest-tp']))
# print('Link 2 Source: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                                    js['network-topology']['topology'][3]['link'][1]['source']['source-tp']))
# print('Link 2 Destination: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                                         js['network-topology']['topology'][3]['link'][1]['destination']['dest-tp']))
# print('Link 3 Source: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                                    js['network-topology']['topology'][3]['link'][2]['source']['source-tp']))
# print('Link 3 Destination: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                                         js['network-topology']['topology'][3]['link'][2]['destination']['dest-tp']))
# print('Link 4 Source: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                                    js['network-topology']['topology'][3]['link'][3]['source']['source-tp']))
# print('Link 4 Destination: ', re.findall('=([0-9]+.[0-9]+.[0-9]+.[0-9]+)',
#                                         js['network-topology']['topology'][3]['link'][3]['destination']['dest-tp']))

# for item in js['comments']:
#    print 'Name: ', item['name']
#    print 'Count: ', item['count']
