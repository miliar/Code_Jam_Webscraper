#include<bits/stdc++.h>
using namespace std;
#define ALL(v) (v).begin(),(v).end()
int main() {
	int T; cin >> T;
	for(int tc=1;tc<=T;tc++) {
		int n, mod; cin >> n >> mod;
		vector<int> K (mod, 0);
		for (int i=0; i<n; i++) {
			int v; cin >> v;
			K[v % mod]++;
		}
		map<vector<int>, int> M;
		vector<int> s (mod, 0);
		deque<vector<int>> Q;
		Q.push_back(s);
		M[s] = 0;
		while (!Q.empty()) {
			vector<int> v = Q.front();
			int s=0;for(int r=0;r<mod;r++)s+=r*v[r];
			Q.pop_front();
			for (int it=0; it<mod; it++) {
				if (v[it] < K[it]) {
					vector<int> v2 = v;
					v2[it]++;
					if (!M.count(v2)) Q.push_back(v2);
					M[v2] = max(M[v2], M[v] + int(s%mod==0));
				}
			}
		}
		cout << "Case #"<<tc<<": "<<M[K] << endl;
	}
}
