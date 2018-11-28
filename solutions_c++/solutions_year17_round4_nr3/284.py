#include <bits/stdc++.h>

using namespace std;
#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)c.size())
#define ten(n) ((int)1e##n)
using ll = long long;
using Pii = pair<int, int>;
using Pll = pair<ll, ll>;

template<typename ...> static inline int getchar_unlocked(void) { return getchar(); }
template<typename ...> static inline void putchar_unlocked(int c) { putchar(c); }
#define mygc(c) (c)=getchar_unlocked()
#define mypc(c) putchar_unlocked(c)
void reader(int& x) { int k, m = 0; x = 0; for (;;) { mygc(k); if (k == '-') { m = 1; break; }if ('0' <= k&&k <= '9') { x = k - '0'; break; } }for (;;) { mygc(k); if (k<'0' || k>'9')break; x = x * 10 + k - '0'; }if (m) x = -x; }
void reader(ll& x) { int k, m = 0; x = 0; for (;;) { mygc(k); if (k == '-') { m = 1; break; }if ('0' <= k&&k <= '9') { x = k - '0'; break; } }for (;;) { mygc(k); if (k<'0' || k>'9')break; x = x * 10 + k - '0'; }if (m) x = -x; }
int reader(char c[]) { int i, s = 0; for (;;) { mygc(i); if (i != ' '&&i != '\n'&&i != '\r'&&i != '\t'&&i != EOF) break; }c[s++] = i; for (;;) { mygc(i); if (i == ' ' || i == '\n' || i == '\r' || i == '\t' || i == EOF) break; c[s++] = i; }c[s] = '\0'; return s; }
int reader(string& c) { int i; for (;;) { mygc(i); if (i != ' '&&i != '\n'&&i != '\r'&&i != '\t'&&i != EOF) break; }c.push_back(i); for (;;) { mygc(i); if (i == ' ' || i == '\n' || i == '\r' || i == '\t' || i == EOF) break; c.push_back(i); }; return sz(c); }
template <class T, class S> void reader(T& x, S& y) { reader(x); reader(y); }
template <class T, class S, class U> void reader(T& x, S& y, U& z) { reader(x); reader(y); reader(z); }
template <class T, class S, class U, class V> void reader(T& x, S& y, U& z, V & w) { reader(x); reader(y); reader(z); reader(w); }
void writer(int x, char c) { int s = 0, m = 0; char f[10]; if (x<0)m = 1, x = -x; while (x)f[s++] = x % 10, x /= 10; if (!s)f[s++] = 0; if (m)mypc('-'); while (s--)mypc(f[s] + '0'); mypc(c); }
void writer(ll x, char c) { int s = 0, m = 0; char f[20]; if (x<0)m = 1, x = -x; while (x)f[s++] = x % 10, x /= 10; if (!s)f[s++] = 0; if (m)mypc('-'); while (s--)mypc(f[s] + '0'); mypc(c); }
void writer(const char c[]) { int i; for (i = 0; c[i] != '\0'; i++)mypc(c[i]); }
void writer(const string& x, char c) { int i; for (i = 0; x[i] != '\0'; i++)mypc(x[i]); mypc(c); }
void writer(const char x[], char c) { int i; for (i = 0; x[i] != '\0'; i++)mypc(x[i]); mypc(c); }
template<class T> void writerLn(T x) { writer(x, '\n'); }
template<class T, class S> void writerLn(T x, S y) { writer(x, ' '); writer(y, '\n'); }
template<class T, class S, class U> void writerLn(T x, S y, U z) { writer(x, ' '); writer(y, ' '); writer(z, '\n'); }
template<class T> void writerArr(T x[], int n) { if (!n) { mypc('\n'); return; }FOR(i, n - 1)writer(x[i], ' '); writer(x[n - 1], '\n'); }
template<class T> void writerArr(vector<T>& x) { writerArr(x.data(), (int)x.size()); }

template<class T> void chmin(T& a, const T& b) { if (a > b) a = b; }
template<class T> void chmax(T& a, const T& b) { if (a < b) a = b; }

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
ll mod_pow(ll a, ll n, ll mod) {
	ll ret = 1;
	ll p = a % mod;
	while (n) {
		if (n & 1) ret = ret * p % mod;
		p = p * p % mod;
		n >>= 1;
	}
	return ret;
}
template<class T> T extgcd(T a, T b, T& x, T& y) { for (T u = y = 1, v = x = 0; a;) { T q = b / a; swap(x -= q * u, u); swap(y -= q * v, v); swap(b -= q * a, a); } return b; }
template<class T> T mod_inv(T a, T m) { T x, y; extgcd(a, m, x, y); return (m + x % m) % m; }
template<class T> T CRT(T m1, T r1, T m2, T r2) { T a1, a2; extgcd(m1, m2, a1, a2); T ret = (m1*a1*r2 + m2*a2*r1) % (m1*m2); return ret < 0 ? ret + m1 * m2 : ret; }

class SCC {
public:
	static const int MV = 5050;
	vector<vector<int> > SC; int NV, GR[MV], rev[MV];
private:
	vector<int> E[MV], RE[MV], NUM; int vis[MV];
public:
	void init(int NV) { this->NV = NV; for (int i = 0; i<MV; i++) { E[i].clear(); RE[i].clear(); } }
	void add_edge(int x, int y) { E[x].push_back(y); RE[y].push_back(x); }
	void dfs(int cu) { vis[cu] = 1; for (int i = 0; i<E[cu].size(); i++) if (!vis[E[cu][i]]) dfs(E[cu][i]); NUM.push_back(cu); }
	void revdfs(int cu, int ind) {
		vis[cu] = 1; GR[cu] = ind; SC[ind].push_back(cu); rev[cu] = ind;
		FOR(i, RE[cu].size()) if (!vis[RE[cu][i]]) revdfs(RE[cu][i], ind);
	}
	void scc() {
		int c = 0; SC.clear(); SC.resize(MV); NUM.clear();
		memset(vis, 0, sizeof(vis)); for (int i = 0; i < NV; i++) if (!vis[i]) dfs(i);
		memset(vis, 0, sizeof(vis)); for (int i = NUM.size() - 1; i >= 0; i--) if (!vis[NUM[i]]) {
			SC[c].clear(); revdfs(NUM[i], c); sort(SC[c].begin(), SC[c].end()); c++;
		}
		SC.resize(c);
	}
};

class TwoSat {
	int NV;
	SCC sc;
public:
	vector<int> val;
	void init(int NV) { this->NV = NV * 2; sc.init(NV * 2); val.resize(NV); }
	void add_edge(int x, int y) { // k+0:normal k+NV:inverse
		sc.add_edge((x + NV / 2) % NV, y);
		sc.add_edge((y + NV / 2) % NV, x);
	}
	bool sat() { // empty:false 
		sc.scc();
		for (int i = 0; i<NV / 2; i++) if (sc.GR[i] == sc.GR[i + NV / 2]) return false;
		for (int i = 0; i < NV / 2; i++) {
			val[i] = sc.GR[i] > sc.GR[i + NV / 2];
		}
		return true;
	}
};

int h, w;
char t[50][51];

const int d[] = { 0,1,0,-1,0 };
vector<int> df;
bool dfs(int a, int b, int dir) {
	if (a < 0 || a >= h || b < 0 || b >= w) return true;
	if (t[a][b] == '|' || t[a][b] == '-') {
		return false;
	}

	if (t[a][b] == '#') return true;
	if (t[a][b] == '/') {
		dir ^= 3;
	} else if (t[a][b] == '\\') {
		dir ^= 1;
	} else {
		df.push_back(a * w + b);
	}
	int na = a + d[dir], nb = b + d[dir + 1];
	bool ret = dfs(na, nb, dir);
	return ret;
}


bool solve() {
	reader(h, w);
	FOR(i, h) reader(t[i]);
	vector<vector<int>> emps(h * w);
	const int U = h * w + 3;
	vector<vector<int>> beams(2 * U);
	vector<bool> beams_ok(2 * U);

	FOR(i, h) FOR(j, w) {
		if (t[i][j] == '|' || t[i][j] == '-') {
			int okcnt = 0;
			FOR(dir, 2) {
				bool ok = true;
				df.clear();
				FOR(k, 2) {
					int ndir = dir + k * 2;
					bool b = dfs(i + d[ndir], j + d[ndir + 1], ndir);
					if (!b) ok = false;
				}
				const int bid = (i * w + j) + dir * U;
				beams_ok[bid] = ok;
				if (ok) {
					okcnt++;
					beams[bid] = df;
					for (auto t : df) {
						emps[t].push_back(bid);
					}
				}
			}
			if (okcnt == 0) return false;
		}
	}

	vector<int> haveto;
	static TwoSat ts;
	ts.init(U);
	const int Fnode = h * w;
	auto make_false_node = [&](int id) {
		const int B = Fnode + 1;
		const int C = Fnode + 2;
		int idOpp = id;
		if (idOpp < U) idOpp += U;
		else idOpp -= U;
		ts.add_edge(idOpp, B);
		ts.add_edge(idOpp, C);
		ts.add_edge(B + U, C + U);
	};
	make_false_node(Fnode);

	FOR(i, h) FOR(j, w) {
		if (t[i][j] == '.') {
			auto& v = emps[i*w + j];
			if (sz(v) == 0) {
				return false;
			} else if (sz(v) == 1) {
				haveto.push_back(v[0]);
				ts.add_edge(v[0], Fnode);
			} else {
				ts.add_edge(v[0], v[1]);
			}
		} else if (t[i][j] == '-' || t[i][j] == '|') {
			const int A = (i * w + j);
			const int B = (i * w + j) + U;
			if (beams_ok[A] && !beams_ok[B]) {
				make_false_node(B);
			} else if (!beams_ok[A] && beams_ok[B]) {
				make_false_node(A);
			}
		}
	}

	bool ans = ts.sat();
	if (!ans) return false;

	if (ts.val[Fnode]) {
		puts("?");
	}

	FOR(i, h) FOR(j, w) {
		if (t[i][j] == '-' || t[i][j] == '|') {
			int id = i * w + j;
			if (ts.val[id] == 1) {
				t[i][j] = '-';
			} else {
				t[i][j] = '|';
			}
		}
	}

	return true;
}

void test() {
	static TwoSat ts;
	const int U = 3;
	ts.init(U);
	const int Fnode = 0;
	{
		const int B = Fnode + 1;
		const int C = Fnode + 2;
		ts.add_edge(Fnode + U, B);
		ts.add_edge(Fnode + U, C);
		ts.add_edge(B + U, C + U);
	}

	bool ok = ts.sat();
	if (!ok) {
		puts("?");
	}
	FOR(i, 3) {
		printf("%d ", ts.val[i]);
	}
	puts("");

}

int main() {
	// test();

	int t; reader(t);
	FOR(i, t) {
		bool ans = solve();
		printf("Case #%d: ", i + 1);
		if (ans) {
			puts("POSSIBLE");
			FOR(j, h) puts(::t[j]);
		} else {
			puts("IMPOSSIBLE");
		}
	}

	return 0;
}