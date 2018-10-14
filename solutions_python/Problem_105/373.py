import networkx as nx
import pkg_resources
pkg_resources.require("matplotlib")
import matplotlib.pylab as plt
import sys

#data = sys.stdin.readlines()
#print "Counted", len(data), "lines."
T = int(sys.stdin.readline())
for i in range(1, T+1):
    N = int(sys.stdin.readline())
    DG = nx.DiGraph()
    for j in range(1,N+1):
        in_ = sys.stdin.readline()
        edges_ = in_.split()
        cnt = 0
        for k in edges_:
            if cnt == 0:
                cnt = 1
            else:
                DG.add_edge(int(j),int(k), capacity = 1.0)
        del edges_[:]
    #print DG.edges()
    #print DG.neighbors(1)
    #let's delete all nodes with indegree 1 and outdegree 0 or indegree 0 and outdegree 1
#    for n_ in DG.nodes():
#        if (DG.in_degree(n_) == 1 and DG.out_degree(n_) == 0) or (DG.in_degree(n_) == 0 and DG.out_degree(n_) == 1):
#            DG.remove_node(n_)
    success = False
    for n_1 in DG.nodes():
        for n_2 in DG.nodes():
            if n_1 != n_2:
                min_c = nx.min_cut(DG, n_1, n_2)
                if min_c >= 2:
                    success = True
                    break
        if success == True:
            break
    #if i == 5: 
    #nx.draw_spring(DG,node_color=[float(DG.degree(v)) for v in DG],node_size=10,with_labels=True,cmap=plt.cm.Reds,)
    #plt.show() 
    #success = False
#    try:
#        top_sort = nx.topological_sort(DG)
#        #if i == 5:
#        #    print top_sort
#        for z in top_sort:
#            if DG.out_degree(z) == 2:
#                success = True
#                #print "node: %d" % (z)
#                break
#    except:
#        success = False
#        #print "bug"
#        #raise
    if success == True:
        print "Case #%d: Yes" % (i)
    else:
        print "Case #%d: No" % (i)
    DG.clear()