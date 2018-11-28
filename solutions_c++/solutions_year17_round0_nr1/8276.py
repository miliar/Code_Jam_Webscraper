#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	tr(c,i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())
#define	endl			'\n'

typedef long long		ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>		vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>		vpii;

const int MX = 1005;

const int MOD = 1000000007;

int main(int argc, char *argv[])
{
#ifdef	HTRINH_UNIT_TEST
	freopen(argv[1],"r",stdin);
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	ios :: sync_with_stdio(false);
	cin.tie(NULL);

	int T,n,k;
	string s;
	cin >> T;
	FOR(testcase,1,T+1) {
		cin >> s >> k;
		string t = s;
		int n = s.length();
		int ans1 = 0;
		FOR(i,0,n) {
			if (i+k-1 >= n) break;
			if (s[i] == '-') {
				++ans1;
				for (int idx = i, cnt = 0; cnt < k; ++idx, ++cnt) {
					if (s[idx] == '-') s[idx] = '+';
					else s[idx] = '-';
				}
			}
		}
		bool ok1 = true;
		for (auto c : s) {
			if (c == '-') {
				ok1 = false;
				break;
			}
		}
		int ans2 = 0;
		s = t;
		FORD(i,n-1,-1) {
			if (i-k+1 < 0) break;
			if (s[i] == '-') {
				++ans2;
				for (int idx = i, cnt = 0; cnt < k; --idx, ++cnt) {
					if (s[idx] == '-') s[idx] = '+';
					else s[idx] = '-';
				}
			}
		}
		bool ok2 = true;
		for (auto c : s) {
			if (c == '-') {
				ok2 = false;
				break;
			}
		}

		if (!ok1 && !ok2) cout << "Case #" << testcase << ": IMPOSSIBLE" << endl;
		else if (ok1 && ok2) cout << "Case #" << testcase << ": " << min(ans1,ans2) << endl;
		else if (ok1) cout << "Case #" << testcase << ": " << ans1 << endl;
		else cout << "Case #" << testcase << ": " << ans2 << endl;
	}
	return 0;
}
