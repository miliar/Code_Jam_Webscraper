
times = input()
for time in range(times):
    x, y = [int(i) for i in raw_input().split()]
    east = "WE"
    west = "EW"
    north = "SN"
    south = "NS"		
    move = ""
    vert = north
    hori = east
    if(x<0):
        hori = west;		
        x = -1*x;
    if(y<0):
        vert = south;
        y = -1*y;
    for i in range(x):
        move += hori;
    for i in range(y):
        move += vert;		
    print "Case #%d: %s" % (time+1, move)



'''
int main(){
	int T;
	cin>>T;
	int index = 1;
	while(index <= T){
		int x,y;
		cin>>x>>y;
		string east = "WE";
		string west = "EW";
		string north = "SN";
		string south = "NS";		
		string move = "";
		string vert = north;
		string hori = east;
		if(x<0){
			hori = west;		
			x = -1*x;
		}
		if(y<0){
			vert = south;
			y = -1*y;			
		}
		for(int i=0; i<x; i++){
			move += hori;		
		}			
		for(int i=0; i<y; i++){
			move += vert;		
		}
		cout<<"Case #"<<index<<": "<<move<<endl;
		index++;
	}
	return 0;
}
'''