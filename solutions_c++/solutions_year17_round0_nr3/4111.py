#include <bits/stdc++.h>
using namespace std;

int main(){
	cin.tie(0);ios_base::sync_with_stdio(0);
	int t;cin>>t;
	for(int i=1;i<=t;i++){
		int n,k;cin>>n>>k;
		priority_queue<int> pq;
		pq.push(n);
		for(int j=0;j<k-1;j++){
			int tp=pq.top();pq.pop();
			tp--;
			int ll=tp/2;
			int rr=tp-ll;
			pq.push(ll);
			pq.push(rr);
		}
		int tp=pq.top();pq.pop();
		tp--;
		int ll=tp/2;
		int rr=tp-ll;
		cout<<"Case #"<<i<<": "<<max(ll,rr)<<" "<<min(ll,rr)<<'\n';
	}
	return 0;
}