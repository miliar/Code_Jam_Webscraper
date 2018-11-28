#include<bits/stdc++.h>
#define int long long
using namespace std;

signed main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		int n,k;cin>>n>>k;
		priority_queue<int> pq;
		pq.push(n);
		int a,b;
		for(int i=0;i<k;i++){
			int x = pq.top();
			pq.pop();
			a = x/2, b = (x-1)/2;
			pq.push(a);pq.push(b);
		}
		cout<<"Case #"<<t<<": "<<a<<" "<<b<<endl;
	}
	return 0;
}
