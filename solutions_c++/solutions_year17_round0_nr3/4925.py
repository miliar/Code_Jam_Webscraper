#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	priority_queue <long long> pq;
	cin>>t;
	long long n,k;
	int man=0;
	while(t--){
		//man++;
		man++;
		cin>>n>>k;
		long long x=n,a,b,c,d;
		for(int i=0;i<k;i++){
			x--;
			a=x/2;
			b=x-a;
			pq.push(a);
			pq.push(b);
			c=min(a,b);
			d=max(a,b);
			x=pq.top();
			pq.pop();	
		}
		cout<<"Case #"<<man<<": "<<d<<" "<<c<<endl;
	//	pq.clear();
		while(!pq.empty()){
			pq.pop();
		}
		
	}
	
	
	
}
