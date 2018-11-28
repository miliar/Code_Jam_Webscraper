#include <vector>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>
using namespace std;


struct Inter{
	int l,r;
	
	Inter(){};
	Inter(int a, int b){
		l = a; r = b;
	}
	
	bool operator<(const Inter& i){
		if((i.r-i.l) != (r-l))
			return (i.r-i.l) < (r-l);
			
		return l > i.l;
	}

};

bool operator<(const Inter& i, const Inter& b) {
 		if((i.r-i.l) != (b.r-b.l))
			return (i.r-i.l) < (b.r-b.l);
			
		return b.l > i.l;
}


int main(){
	freopen ("C-small-2-attempt0.in","r",stdin);
	freopen ("myff","w",stdout);
	int i,q,k,t,j,l,r,n;
	
	cin>>t;
	string c, x;
	for(q = 1; q<=t; q++){
		priority_queue<Inter> pq;
		Inter in;
		
		cin>>n>>k;
		in.l = 0;
		in.r = n+1;
		pq.push(in);
		int rr,rl;
		
		for(i = 1; i <=k; i ++){
			in = pq.top();
			pq.pop();
			
			l = in.l;
			r = in.r;
			
		//	cout<<l<<" "<<r<<endl;
			
			j = l+(r-l)/2;
			
			in.r = j;
			pq.push(in);
			in.l = j;
			in.r = r;
			
			pq.push(in);
			
			rl = j-l-1;
			rr = r-j-1;
						
		}
		
		if(rr>rl)
			swap(rr,rl);
		
		cout<<"Case #"<<q<<": "<<rl<<" "<<rr<<endl;
		
	}
	
	
	
	return 0;
	
}
