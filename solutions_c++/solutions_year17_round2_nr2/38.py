#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define nfor(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; } 
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const map<X, Y>& a) { return out << vector<pair<X, Y>>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, pair<T*, int> a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

#ifdef SU1
#define LOG
#endif

int n, r, o, y, g, b, v;

bool read() {
	if (!(cin >> n >> r >> o >> y >> g >> b >> v))
		return false;
	return true;
}

map <char, char> mt;
map <char, pt> gr;

void print(char c) {
	putchar(c);
	if (gr[c].x > 0) {
		forn(_, gr[c].y) {
			printf("%c%c", mt[c], c);
		}
		gr[c].x--;
		gr[c].y = 1;
	}
}

void init() {
	b -= o; gr['B'] = mp(1, o);
	r -= g; gr['R'] = mp(1, g);
	y -= v; gr['Y'] = mp(1, v);
}

void solve(int tc) {
	mt['B'] = 'O';
	mt['R'] = 'G';
	mt['Y'] = 'V';


	printf("Case #%d: ", tc + 1);

	if (b == o && n == b + o) {
		forn(i, b)
			printf("BO");
		puts("");
		return;
	}

	if (r == g && n == r + g) {
		forn(i, r)
			printf("RG");
		puts("");
		return;
	}

	if (y == v && n == y + v) {
		forn(i, y)
			printf("YV");
		puts("");
		return;
	}

	if ((b > 0 && b <= o) || (r > 0 && r <= g) || (y > 0 && y <= v)) {
		puts("IMPOSSIBLE");
		return;
	}

	init();
//	cerr << r << " " << y << " " << b << endl;
	int sum = r + y + b;
	vector <pair <int, char> > v(3);
	v[0] = mp(r, 'R');
	v[1] = mp(y, 'Y');
	v[2] = mp(b, 'B');
	sort(all(v));

	if (v[2].x > sum - v[2].x) {
		puts("IMPOSSIBLE");
		return;
	}

//	cerr << v[2].x << endl;
//	cerr << gr['Y'] << endl;


	while (v[2].x) {
		print(v[2].y);
		if (v[0].x + v[1].x == v[2].x) {
			if (v[0].x) {
				print(v[0].y);
				--v[0].x;
			} else {
				print(v[1].y);
				--v[1].x;
			}
		} else {
			print(v[0].y);
			--v[0].x;
			print(v[1].y);
			--v[1].x;
		}
		--v[2].x;
	}
	puts("");
}

int main() {
#ifdef SU1
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

	int t;
	assert(cin >> t);

	int tc = 0;
    while (read()) {
		ld stime = gett();
		solve(tc++);
		cerr << "Time: " << gett() - stime << endl;
		//break;
	}
	
    return 0;
}
