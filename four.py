from igraph import *

g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
print(g.vs)
g.vs['name'] = ['Alice', 'Bob', 'Claire', 'Dennis', 'Esther', 'Frank', 'George']
g.vs['age'] = [25, 31, 18, 47, 22, 23, 50]
g.vs['gender'] = ['f', 'm', 'f', 'm', 'f', 'm', 'm']
g.es['is_formal'] = [False, False, True, True, True, False, True, False, False]

print(g.es[0])
print(g.es[0].attributes())
g.es[0]['is_formal']  = True
print(g.es[0])
g['date'] = '2009-01-10'
print(g.degree())
print(g.degree(6))
print(g.degree([2, 3, 4]))

print(g.vs.select(_degree = g.maxdegree())['name'])
claire = g.vs.find(name='Claire')
print type(claire)

layout = g.layout('kk')

g.vs["label"] = g.vs["name"]
color_dict = {"m": "blue", "f": "pink"}
g.vs["color"] = [color_dict[gender] for gender in g.vs["gender"]]
plot(g, layout = layout, bbox = (300, 300), margin = 20)
