#include<bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define rep(i,a,b) for(i=a;i<=b;i++)
#define rep2(i,a,b,c) for(i=a;i<=b;i+=c)

priority_queue<int> pq;

int main(){
	freopen("CCC.in","r",stdin);
	freopen("CCC.out","w",stdout);
	int n,k,cas=0;
	int tes,tt;
	cin>>tes;
	while(tes--){
		while(!pq.empty()){
			pq.pop();
		}
		cas++;
		cin>>n>>k;
		pq.push(n);
		k--;
		while(k--){
			tt=pq.top();pq.pop();
			pq.push(tt/2);
			pq.push((tt-1)/2);
		}
		tt=pq.top();
		cout<<"Case #"<<cas<<": "<<tt/2<<" "<<(tt-1)/2<<"\n";
	}
}
 
