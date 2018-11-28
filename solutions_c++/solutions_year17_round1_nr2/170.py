#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define REP(i,n) for(int i=0; i < (n); ++i)
#define SIZE(c) (int) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define FWD(i,a,b) for (int i=(a); i<(b); ++i)
#define BCK(i,a,b) for (int i=(a); i>(b); --i)
#define PI 3.14159265358979311600
#define pb push_back
#define mp make_pair
#define st first
#define nd second

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

typedef vector < int > VI;
typedef vector<ll> VL;

typedef long double K;

const int N = 55;

int n, p;
int a[N][N], amount[N], l[N][N], r[N][N];

void solve() {
	cin >> n >> p;
	REP(i, n) cin >> amount[i];
	vector<deque<pair<int,int>>> g(n);
	vector<int> cmp;
	REP(i, n) {
		REP(j, p) {
			cin >> a[i][j];
			int curL = (a[i][j] * 10 + 10) / 11;
			int curR = (a[i][j] * 10) / 9;
			curL = (curL + amount[i] - 1) / amount[i];
			curR /= amount[i];
			if (curL <= curR) {
				g[i].emplace_back(curL, curR);
				cmp.push_back(curL);
				cmp.push_back(curR);
			}
		}
	}
	sort(cmp.begin(), cmp.end());
	cmp.erase(unique(cmp.begin(), cmp.end()), cmp.end());
	REP(i, n) {
		sort(g[i].begin(), g[i].end());
	}
	vector<multiset<int>> s(n);
	int result = 0;
	for (auto& x : cmp) {
		REP(i, n) while (!g[i].empty() && g[i].front().first <= x) {
			s[i].insert(g[i].front().second);
			g[i].pop_front();
		}
		REP(i, n) while (!s[i].empty() && (*s[i].begin()) < x) s[i].erase(s[i].begin());
		while (true) {
			bool all = true;
			REP(i, n) all &= !s[i].empty();
			if (all) {
				++result;
				REP(i, n) s[i].erase(s[i].begin());
			} else {
				break;
			}
		}
	}
	cout << result << '\n';
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	REP(i, t) {
		cerr << i << endl;
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}