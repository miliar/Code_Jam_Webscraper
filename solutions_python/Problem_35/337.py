#
#google code jam watersheds problem
#
import sys

MAX_ALTITUDE=10000

class drainage_basins:
    name=""

T=sys.stdin.readline()
T=int(T)
maps=[]
label_maps=[]
maps_height=[]
maps_width=[]

map_altitudes=[]

alphabets= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


for i in range(T):
    H,W=sys.stdin.readline().split()
    H=int(H)
    W=int(W)
    maps_height.append(H)
    maps_width.append(W)
    maps.append([])
    label_maps.append([])
    map_altitudes.append([])
    map_altitudes[i]=[]
    for l in range(MAX_ALTITUDE):
        map_altitudes[i].append([])
    for j in range(H):
	row=sys.stdin.readline().split()
	maps[i].append([])
	label_maps[i].append([])
	for k,cell in enumerate(row):
            cell=int(cell)
       	    maps[i][j].append(cell)
	    label_maps[i][j].append(0)
	    map_altitudes[i][cell].append((j,k))



for Map,altitudes in enumerate(map_altitudes):
    for altitude,cordinates in enumerate(altitudes):
        for i,j in cordinates:
            if label_maps[Map][i][j]==0:
                label_maps[Map][i][j]= drainage_basins()
            if ((i+1) < maps_height[Map])  and label_maps[Map][i+1][j]==0 and  (maps[Map][i+1][j] > maps[Map][i][j]):
                label_maps[Map][i+1][j]=label_maps[Map][i][j]
            if ((j+1) < maps_width[Map])  and label_maps[Map][i][j+1]==0 and (maps[Map][i][j+1] > maps[Map][i][j]):
                label_maps[Map][i][j+1]=label_maps[Map][i][j]                        
            if  j > 0   and  label_maps[Map][i][j-1]==0 and (maps[Map][i][j-1] > maps[Map][i][j]):
                label_maps[Map][i][j-1]=label_maps[Map][i][j]
            if  i > 0   and label_maps[Map][i-1][j]==0 and (maps[Map][i-1][j] > maps[Map][i][j]):
                label_maps[Map][i-1][j]=label_maps[Map][i][j]
                        


for k,label_map in enumerate(label_maps):
    alpha_no=0
    print "Case #%s:" % (k+1)
    for row in label_map:
        row_cells=[]
        for cell in row:
            if cell.name=="":
                cell.name=alphabets[alpha_no]
                alpha_no+=1
            row_cells.append(cell.name)
        print  " ".join(row_cells)

