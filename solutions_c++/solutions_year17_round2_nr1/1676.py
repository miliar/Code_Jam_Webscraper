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


int main(){
	
	freopen("zoki.in","r",stdin);
	freopen("myf.txt","w",stdout);
	set<int> s;
	
	int i,j,k,q,t,r,n;
	double l,h,m,res;
	cin>>t;
	Node no;
	for(q = 1; q<=t;q++){
		vector<Node> vec;
		cin>>k>>n;
		
		for(i = 0; i<n; i ++){
			cin>>no.pos>>no.brz;
			vec.push_back(no);
		}					
		
		sort(vec.begin(),vec.end());
		double mx = 0;
		double rr;
		for(i = 0; i <n; i ++){
			
			rr = (double)(k-vec[i].pos)/(double)vec[i].brz;
			mx = max(rr,mx);
						
		}
		
		res = (double)k/mx;
			
		
		printf("Case #%d: %.6lf\n",q,res);
		
	}
	

		
	
	return 0;
}
