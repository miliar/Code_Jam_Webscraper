#include "bits/stdc++.h"

#define debug(x) cout<<#x<<": "<<x<<endl
#define rep(i,n) for (int i=0;i<(n);i++)
#define FOR(i,a,b) for (int i=(a);i<=(b);i++)
#define all(a) (a).begin(),(a).end()
using namespace std;
typedef vector<int> VI;
typedef vector<vector<int>> VVI;
typedef long long ll;

void solve() {
#ifdef _WIN32
	istream &cin = ifstream("input.txt");
#endif
	int n;
	cin >> n;
	rep(i, n) {
		string s;
		int k;
		cin >> s >> k;

		int initial = 0;
		rep(j, s.size()) {
			if (s[j] == '+') initial |= (1 << j);
		}
		vector<int> v(1 << s.size(), -1);
		queue<int> q;
		q.push(initial);
		v[initial] = 0;

		if (initial == ((1 << s.size()) - 1)) {
			cout << "CASE #" << i + 1 << ": " << 0 << endl;
			continue;
		}
		bool found = false;
		while (q.size() > 0) {
			int state = q.front(); q.pop();
			
			rep(j, s.size() - k + 1) {
				int newstate = state ^ (((1 << k) - 1) << j);
				
				if (newstate == ((1 << s.size()) - 1)) {
					found = true;
					cout << "CASE #" << i + 1 << ": " << v[state] + 1 << endl;
					break;
				} else {
					if (v[newstate] == -1 || v[newstate] > v[state] + 1) {
						v[newstate] = v[state] + 1;
						q.push(newstate);
					}
					
				}
			}
			if (found) break;
		}
		if (!found) cout << "CASE #" << i + 1 << ": IMPOSSIBLE" << endl;
	}
}




int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);


	solve();
#ifdef _WIN32
	system("PAUSE");
#endif
	return 0;
}