import sys,re

#ver1: (1) identify sinks and label them, left to right, top to bottom
#      (2)the elevation map is a directed graph, calculate its transpose
#      (3)find nodes connected to sinks identified in (1) using bfs and label
#         these with the sink names



h,w=0,0
cases=0
def process_data(filename,fout):
    global h,w,cases
    f=open(filename)
    fw=open(fout,'w')
    mapread=False
    mapstart,mapend=0,0
    elv_map=[]
    lineno=0
    curr_case_no=0
    for line in f:
        line=line.strip()
        lineno+=1
        if(lineno==1):
            cases = int(line)
            continue
        if(not mapread):
            elv_map=[]
            h,w = map(lambda(x):int(x) , re.compile(r'\s+').split(line))
            mapread=True
            curr_case_no+=1        
            mapstart = lineno+1
            mapend = lineno + h
            continue
        if(mapread):
            elv_map.append( map(lambda(x):int(x),re.compile(r'\s+').split(line)))

            if(lineno==mapend):
                mapread=False
                #print elv_map
                fw.write('Case #%d:\n'%(curr_case_no))
                basin = calc_basin(elv_map)
                print curr_case_no
                for elem in basin:
                    fw.write('%s\n'%(' '.join(elem)))
                    fw.flush()
                    
                


    f.close()
    fw.close()
    print 'Cases:',cases


def calc_basin(elv_map):
    '''Calculates the final answer - the master function of sorts.'''
    adj,sink = createadj(elv_map)
    sym = traverse(adj,sink)
    lexlabel(sym)
    return sym

def createadj(elv_map):
    adj={}
    sinklist=[]
    for i in range(h):
        for j in range(w):
            minval=elv_map[i][j]
            mincell=None
            for nbr in [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]:
                x,y=nbr
                
                if((x<0 or x>=h ) or (y<0 or y>=w)):continue
                #print 'neigbor:',nbr
                if(elv_map[x][y] < minval):
                    minval= elv_map[x][y]
                    mincell = nbr
            #print (i,j), mincell,minval
            if(mincell!=None):
                if(mincell not in adj.keys()):adj[mincell]=[]
                adj[mincell].append((i,j))
            else: sinklist.append((i,j))
    return adj,sinklist



def traverse(adj,sinklist):
    BLACK,GRAY,WHITE = 1,0,-1
    sym_map,color=[],[]
    symdef,colordef=[],[]
    for i in range(w):
        symdef.append(None)
        colordef.append(WHITE)
    for i in range(h):
        sym_map.append(symdef[:])
        color.append(colordef[:])
    #print color,sym_map
    curr_sym=0  #basin number

    #do a bfs from the sinks, and label a drainage basin
    for s in sinklist:
        curr_sym+=1
        q=[s]
        #color is a dd array created using h,w, initialised to -1 so is sym_map
        color[s[0]][s[1]]=GRAY
        sym_map[s[0]][s[1]] = curr_sym
        
        while(len(q)>0):
            #print q
            curr=q[0]
            del q[0]
            if(curr in adj.keys()):
                for v in adj[curr]:
                    if(color[v[0]][v[1]]==WHITE):
                        color[v[0]][v[1]]=GRAY
                        q.append(v)
                        sym_map[v[0]][v[1]]= curr_sym
            color[curr[0]][curr[1]]=BLACK
    return sym_map




def lexlabel(sym_map):
    '''Do lexicographic labelling of symmap'''
    lexmap={}
    alph=map(chr, range(97, 123))
    alph_idx=0
    for i in range(h):
        for j in range(w):
            if(sym_map[i][j] in lexmap.keys()):  sym_map[i][j] = lexmap[sym_map[i][j]]
            else:
                lexmap[sym_map[i][j]]=alph[alph_idx]
                sym_map[i][j] = alph[alph_idx]
                alph_idx+=1

    
        
