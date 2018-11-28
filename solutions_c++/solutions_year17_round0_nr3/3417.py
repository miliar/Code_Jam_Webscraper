#include <bits/stdc++.h>
using namespace std;

int t,n,k;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> n >> k;
		priority_queue<int> pq;
		pq.push(n);
		int mn,mx;
		while (k--){
			int now=pq.top();
			pq.pop();
			mn=(now-1)>>1;
			mx=now-1-mn;
			if (mn) pq.push(mn);
			if (mx) pq.push(mx);
		}
		cout << mx << " " << mn << "\n";
	}
}
