#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair< ii , int > pii;
#define endl '\n'
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ll long long
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(decltype((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define FASTIO (ios_base::sync_with_stdio(0),cout.tie(0),cin.tie(0))
#define TIME_S clock_t tStart = clock()
#define TIME_E printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC)
const int INF = 1e9;
/*codejam_2017_B_1B*/

int order = 0;
char maxone(int &r, int &y, int &b) {
	if (order == 0) {
		if (r >= y and r >= b) {
			r--;
			return 'R';
		}
		if (b >= y and b >= r) {
			b--;
			return 'B';
		}
		if (y >= b and y >= r) {
			y--;
			return 'Y';
		}
	}
	if (order == 1) {
		if (b >= y and b >= r) {
			b--;
			return 'B';
		}
		if (r >= y and r >= b) {
			r--;
			return 'R';
		}
		if (y >= b and y >= r) {
			y--;
			return 'Y';
		}
	}
	if (order == 2) {
		if (y >= b and y >= r) {
			y--;
			return 'Y';
		}
		if (b >= y and b >= r) {
			b--;
			return 'B';
		}
		if (r >= y and r >= b) {
			r--;
			return 'R';
		}
	}
}
int main() {
	// FASTIO;
	int t;
	cin >> t;
	REP(c, t) {
		int n;
		cin >> n;
		int r, o, y, g, b, v;
		string ans;
		bool status = true;
		cin >> r >> o >> y >> g >> b >> v;
		if ( o == 0 and g == 0 and v == 0) {
			while (r != 0 or y != 0 or b != 0) {
				char x = maxone(r, y, b);
				if (sz(ans) > 0) {
					int t = -1;
					if (x == 'R' and ans[sz(ans) - 1] == 'R') {
						if (y != 0 or b != 0) {
							r++;
							x = maxone(t, y, b);
						}
					}
					else if (x == 'Y' and ans[sz(ans) - 1] == 'Y') {
						if (r != 0 or b != 0) {
							y++;
							x = maxone(r, t, b);
						}
					}
					else if (x == 'B' and ans[sz(ans) - 1] == 'B') {
						if (r != 0 or y != 0) {
							b++;
							x = maxone(r, y, t);
						}
					}
				}
				if (sz(ans) == 0) {
					if (x == 'R')	order = 0;
					if (x == 'B')	order = 1;
					if (x == 'Y')	order = 2;
				}
				// cout << order << endl;
				ans.pb(x);
				// cout << ans <<endl;
			}
			REP(i, sz(ans)) {
				if (ans[i] == ans[(i + 1) % n])
					status = false;
			}
		}
		// status = true;
		if (status)
			cout << "Case #" << c + 1 << ": " << ans << endl;
		else {
			cout << "Case #" << c + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
}
