#include <cmath>
#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
using namespace std;

struct Node{
	int brz, pos;
	Node(){
	}
			
};

bool operator<(const Node &a, const Node &b){
	
	if(a.pos!=b.pos)
		return a.pos>b.pos;
	
	return a.brz<b.brz;
}
//425 112 0 130 0 183 0

int main(){
	
	freopen("B-small-attempt1.in","r",stdin);
	freopen("myf.txt","w",stdout);
	set<int> s;
	
	int i,j,k,q,t,r,n,o,y,g,b,v;//{R, O, Y, G, B, V}.
	double l,h,m;
	cin>>t;
	Node no;
	for(q = 1; q<=t;q++){
		vector<Node> vec;
		string res;
		cin>>n>>r>>o>>y>>g>>b>>v;
		
		int R,Y,B;
		char prev = 'Z';
		
		R=r;Y=y;B=b;
		
		if(r>=y && r>=b){
			prev = 'R';
			res="R";
			r--;
		}
		else if (y>=b){
			prev='Y';res="Y";y--;
		}
		else{
			res = "B";prev='B';b--;
		}
		

		
		for(i = 1; i<n; i ++){
			
			
			if(prev =='R'){
				
				
				if(Y>=B){
				
				if(y && y>=b){
				prev = 'Y';
				res+="Y";
				y--;
				continue;
				}
				
				if(b){
				prev = 'B';
				res+="B";
				b--;
				continue;
		
				}
			}
			else{
			if(b && b>=y){
					prev = 'B';
				res+="B";
				b--;
				continue;
		
			
				}
				
				if(y){
				prev = 'Y';
				res+="Y";
				y--;
				continue;
				}
				
			}
				
			}
			
			if(prev == 'Y'){
				
				if(R>=B){
				
				if(r && r>=b){
				prev = 'R';
				res+="R";
				r--;
				continue;
				}
				
				
				
				if(b){
				prev = 'B';
				res+="B";
				b--;
				continue;
		
				}
			}else{
				
				if(b && b>=r){
					prev = 'B';
				res+="B";
				b--;
				continue;	
					
			
				}
				
				
				
				if(r){
				prev = 'R';
				res+="R";
				r--;
				continue;
		
				}
				
				
			}
				
			}
			
			
				if(prev == 'B'){
				if(R>=Y){
				
				if(r && r>=y){
				prev = 'R';
				res+="R";
				r--;
				continue;
				}
				
				
				
				if(y){
				prev = 'Y';
				res+="Y";
				y--;
				continue;
		
				}
			}
			else{
				
				if(y && y>=r){
						prev = 'Y';
				res+="Y";
				y--;
				continue;
			
				}
				
				
				
				if(r){
				prev = 'R';
				res+="R";
				r--;
				continue;
		
				}
				
				
			}
			}
			
			
	//		cout<<"<MMM "<<res<<endl;
			res = "IMPOSSIBLE";
			break;
		}		
		if(res!="IMPOSSIBLE"){
		
		if(res[0]==res[n-1]){
	//	cout<<"ZZZ "<<res<<endl;		
			res = "IMPOSSIBLE";
	}
}
		
		printf("Case #%d: %s\n",q,res.c_str());
		
	}
	

		
	
	return 0;
}
