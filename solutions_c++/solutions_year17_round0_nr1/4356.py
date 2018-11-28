#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())
typedef long long ll;

int t;

int main(int argc, char const *argv[]) {
	ios_base::sync_with_stdio(false);
	cin >> t;
	int res[105];
	fill(res, res+t, 0);
	FOR(i, t) {
		string s;
		int k;
		cin >> s >> k;

		vector<int> v(s.size());
		FOR(j, s.size()) {
			if (s[j] == '+') v[j] = 1;
			else v[j] = -1;
		}
		
		FOR(j, v.size()-k+1) {
			if (v[j] == -1) {
				FOR(cnt, k) v[j+cnt] *= -1;
				res[i]++;
			}
		}
		bool flag = false;
		FOR(j, v.size()) {
			if (v[j] == -1) {
				flag = true;
				break;
			}
		}
		if (flag) res[i] = -1;
	}
	FOR(i, t) {
		if (res[i] == -1) cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << i+1 << ": " << res[i] << endl;
	}
	return 0;
}