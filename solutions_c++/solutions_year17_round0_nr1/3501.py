#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define REP(i,k,n) for(int i=k;i<(int)(n);i++)
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
#define INF 1<<30
#define mp make_pair
#define fi first
#define se second

using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int main() {
	int T;
	cin >> T;

	rep(t, T) {
		string s;
		int n;
		cin >> s >> n;

		int ans = 0;

		rep(i, s.size()) {
			if(i + n <= s.size() && s[i] == '-') {
				rep(j, n) {
					if(s[i + j] == '-') {
						s[i + j] = '+';
					} else {
						s[i + j] = '-';
					}
				}
				ans++;
			}
		}

		bool flag = true;
		rep(i, s.size()) {
			if(s[i] == '-') flag = false;
		}

		cout << "Case #" << t + 1 << ": ";

		if(flag) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
