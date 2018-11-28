#include <bits/stdc++.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;

string s = "ROYGBV";
int a[6];
int n;

inline bool read() {
	cin >> n;
	forn (i, 6)
		cin >> a[i];
	return true;
}

string t[] = {
	"RG",
	"YV",
	"BO"
};



bool can(string &ans, int c[3]) {
	while(true) {
		bool done = false;
		forn (i, 3)
			if (c[i] <= 1)
				done = true;
		forn (i, 3) {
			if (c[i] > c[(i + 1) % 3] + c[(i + 2) % 3] - 10)
				done = true;
		}
		if (done)
			break;
		string f = "RYB";
		if (sz(ans) && ans.back() == 'R')
			f = "YRB";
		ans += f;
		forn (i, 3)
			c[i]--;	
	}
	forn (i, 3)
		cerr << c[i] << ' ';
	cerr << endl;
	forn (r, 3) {
		queue<pair<pt, pt> > q;
		set<pair<pt, pt> > used;
		if (sz(ans) && ((int)s.find(ans.back()) / 2 != r))
			continue;
		if (!sz(ans))
			c[r]--;
		q.push(mp(mp(r, c[0]), mp(c[1], c[2])));
		used.insert(mp(mp(r, c[0]), mp(c[1], c[2])));
		if (!sz(ans))
			c[r]++;
		while(!q.empty()) {
			int last = q.front().x.x;
			int a[3] = {q.front().x.y, q.front().y.x, q.front().y.y};
			q.pop();
			forn (i, 3) {
				if (i == last || a[i] == 0)
					continue;
				a[i]--;
				bool ok = true;
				forn (j, 3) {
					if (a[j] > a[(j + 1) % 3] + a[(j + 2) % 3] + 2)
						ok = false;
				}
				if (ok && !used.count(mp(mp(i, a[0]), mp(a[1], a[2])))) {
					used.insert(mp(mp(i, a[0]), mp(a[1], a[2])));
					q.push(mp(mp(i, a[0]), mp(a[1], a[2])));
				}
				a[i]++;
			}
		}
		int f = -1;
		forn (i, 3) {
			if (used.count(mp(mp(i, 0), mp(0, 0))))
			if (i != r)
				f = i;
		}
		if (f == -1)
			continue;
		int a[3] = {0, 0, 0};
		string suf = "";
		while(a[0] != c[0] || a[1] != c[1] || a[2] != c[2]) {
			a[f]++;
			suf += s[f * 2];
			int nt = -1;
			forn (i, 3)
				if (i != f && used.count(mp(mp(i, a[0]), mp(a[1], a[2]))))
					nt = i;
			f = nt;
			if (a[0] != c[0] || a[1] != c[1] || a[2] != c[2])
				assert(nt != -1);
		}
		reverse(all(suf));
		ans += suf;
		return true;
	}
	return false;
}

inline void solve() {   
	string ans = "";
	if (n == 1) {
		forn (i, 6)
			if (a[i])
				cout << s[i] << endl;
		return;
	}
	forn (it, 3) {
		int i = s.find(t[it][0]);
		int j = s.find(t[it][1]);
		if (a[i] + a[j] == n && a[i] == a[j]) {
			forn (it, a[i])
				cout << s[i] << s[j];
			cout << endl;
			return;
		}
	}
	forn (it, 3) {
		int i = s.find(t[it][0]);
		int j = s.find(t[it][1]);
		if (!a[j])
			continue;
		if (a[i] < a[j] + 1) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		ans += s[i];
		forn (k, a[j])
			ans += s[j], ans += s[i];
		a[i] -= a[j] + 1;
	}
	int c[3] = {a[0], a[2], a[4]};
	if (can(ans, c))
		cout << ans << endl;
	else
		cout << "IMPOSSIBLE" << endl;
}

int main()
{
#ifdef SU2
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(6) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));

	int t;
	cin >> t;
	forn (i, t) {
		read();
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

#ifdef SU2
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}