#pragma GCC target("sse4.1")
#pragma GCC optimize("O3")
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back

mt19937 rnd;

template<class T> inline void opt (T &a, T b) {
	a = min (a, b);
}

inline int rndInt (int x) {
	return rnd () % x;            
}

inline int R (int l, int r) {
	return l + rndInt (r - l + 1);
}

char Cur;

inline char getChar () {
	char t = Cur;
	Cur = getchar ();
	return t;
}

template<class telem> void readInt (telem &a) {
	a = 0;
	while (!isdigit (Cur)) getChar ();
	while (isdigit (Cur)) {
		a *= 10;
		a += getChar () - '0';
	}
}

typedef long double dbl;

int T = 1;
int n;
ll dst[111][111];
const ll inf = 1e10;
int E[111];
dbl s[111];
int Q;
int S[11111], Tt[11111];

void pre () {

}                                   

void load () {
	cin >> n >> Q;
	for (int i = 0; i < n; i++) {
		cin >> E[i] >> s[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> dst[i][j];
			if (dst[i][j] == -1)
				dst[i][j] = inf;
		}
		dst[i][i] = 0;
	}
	for (int i = 0; i < Q; i++) {
		cin >> S[i] >> Tt[i];
		S[i] --;
		Tt[i] --;
	}
}

dbl D[111];
struct comp {
	bool operator () (int a, int b) {
		if (abs (D[a] - D[b]) < 1e-7)
			return a < b;
		return D[a] < D[b];
	}
};

void dijkstra (int v, int t) {
	clog << v << ' ' << t << endl;
	fill (D, D + n, 1e30);
	D[v] = 0;
	set<int, comp> q;
	q.insert (v);
	while (q.size ()) {
		v = *q.begin ();
		//clog << v << ' ' << D[v] << endl;
		q.erase (q.begin ());
		for (int i = 0; i < n; i++) {
			if (i == v) continue;
			if (dst[v][i] <= E[v]) {
				if (D[i] > D[v] + 1.0 * dst[v][i] / s[v]) {
					q.erase (i);
					opt (D[i], D[v] + 1.0 * dst[v][i] / s[v]);
					q.insert (i);
				}
			}
		}
	}
	cout.precision (20);
	cout << fixed << showpoint;
	cout << D[t] << ' ';
	fflush (stdout);
}

void solve (int tc) {
	clog << tc << endl;
	cout << "Case #" << tc << ": ";

	for (int k = 0; k < n; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				opt (dst[i][j], dst[i][k] + dst[k][j]);
			}
		}
	}
	for (int i = 0; i < Q; i++)
		dijkstra (S[i], Tt[i]);
	cout << '\n';
}
	

int main () {
	ios_base::sync_with_stdio (false);
	cin.tie (0);
	pre ();
#ifdef LOCAL
	auto ___ = freopen ("file.in", "r", stdin);
	___ = freopen ("file.out", "w", stdout);
	assert (___);
#endif

	double st = clock ();

	cin >> T;
	int tc = 0;

	while (T --> 0) {
		tc++;	
		load ();  
		solve (tc);
	}

	clog << (clock () - st) / CLOCKS_PER_SEC << endl;

	return 0;
}