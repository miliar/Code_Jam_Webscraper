#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;

int n, m, a[51][51], c[51];

int solve(){
	cin >> n >> m;
	for(int i=0; i<n; i++){
		cin >> c[i];
	}
	vector<pi> v[51];
	vector<int> ev;
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			cin >> a[i][j];
			int ed = (a[i][j] * 10) / (9 * c[i]);
			int st = (a[i][j] * 10 + 11 * c[i] - 1) / (11 * c[i]);
			if(st <= ed){
				ev.push_back(st);
				ev.push_back(ed+1);
				v[i].push_back(pi(st, ed));
			}
		}
	}
	sort(ev.begin(), ev.end());
	ev.resize(unique(ev.begin(), ev.end()) - ev.begin());
	priority_queue<int, vector<int>, greater<int> > pq[55];
	int ans = 0;
	for(int i=0; i<ev.size(); i++){
		for(int j=0; j<n; j++){
			for(auto &k : v[j]){
				if(ev[i] == k.first) pq[j].push(k.second);
			}
		}
		int mx = 1e9;
		for(int j=0; j<n; j++){
			while(!pq[j].empty() && pq[j].top() < ev[i]){
				pq[j].pop();
			}
			mx = min(mx, (int)pq[j].size());
		}
		ans += mx;
		for(int j=0; j<n; j++){
			for(int k=0; k<mx; k++) pq[j].pop();
		}
	}
	return ans;
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: %d\n", i, solve());
	}
}
