_species:
tree_features[species] = tree_features[species].mean()
def sim_measure(a, b, method):
if method == 'scalar':
return a.dot(b)
elif method == 'euclidean distance':
return 1.0/(np.linalg.norm(a.values-b.values)+0.0001)
similarity = {}
for species1 in tree_species:
similarity[species1] = {}
for species2 in tree_species:
similarity[species1][species2] = sim_measure(tree_features[species1],tree_features[species2], 'euclidean distance')
gr = nx.Graph()
for species1 in tree_species:
for species2 in tree_species:
if tree_species.index(species1) < tree_species.index(species2):
gr.add_edge(species1, species2, weight=100*similarity[species1][species2])
pos=nx.spring_layout(gr, iterations=10000, seed = 2) #i like seed (0
P.figure(figsize=(15,15))
P.title('Euclidean Distance Similarity')
P.gca().axis('off')
nx.draw_networkx_edges(gr,pos,edge_color='lightgray')
nx.draw_networkx_nodes(gr,pos,node_color='c', edgecolors ='black', node_size=13)
nx.draw_networkx_labels(gr,pos, {label:r'$\it{'+label.replace(' ',r'\ ')+'}$' for label in tree_species}, font_color='black', verticalalignment='bottom')
P.show()
