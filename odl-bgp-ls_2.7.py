import urllib2
import json
import re
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# url = raw_input ('Enter URL: ')

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

url = 'http://10.62.60.51:8181/restconf/operational/network-topology:network-topology'

password_mgr.add_password(None, url, 'admin', 'admin')

print('Retrieving', url)

handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
#opener.open(url)
urllib2.install_opener(opener)

uh = urllib2.urlopen(url)
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

#nx.write_graphml(G, '%s_graphml' % 'table')
nx.draw(G)
plt.show()
