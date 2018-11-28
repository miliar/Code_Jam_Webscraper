#pragma comment(linker, "/STACK:32000000")
#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0, _= (n); i < _; ++i)
#define DWN(i, n) for (int i = (n) - 1; i >= 0; --i)
#define RE1(i, n) for (int i = 1, _= (n); i <= _; ++i)
#define DW1(i, n) for (int i = (n); i > 0; --i)
#define FOR(i, l, r) for (int i = (l), _ = (r); i < _; ++i)
#define EDGE(u, v, e) for (int e = head[u], v; e != nil && (v = to[e], true); e = next[e])

using namespace std;
typedef long long int64;
inline bool read(int& val)    { return scanf("%d",    &val) != -1;}
inline bool read(int64& val)  { return scanf("%lld", &val) != -1;}
inline bool read(double& val) { return scanf("%lf",   &val) != -1;}
inline bool read(char* val)   { return scanf("%s",     val) != -1;}
template<class T1, class T2>
inline bool read(T1& a, T2& b)
{ return read(a) && read(b); }
template<class T1, class T2, class T3>
inline bool read(T1& a, T2& b, T3& c)
{ return read(a) && read(b) && read(c); }
template<class T1, class T2, class T3, class T4>
inline bool read(T1& a, T2& b, T3& c, T4& d)
{ return read(a) && read(b) && read(c) && read(d); }
template<class T1, class T2, class T3, class T4, class T5>
inline bool read(T1& a, T2& b, T3& c, T4& d, T5& e)
{ return read(a) && read(b) && read(c) && read(d) && read(e); }

const int N = 1111;
struct LR {
	int ls, rs, i;
	friend bool operator<(LR a, LR b) {
		if (min(a.ls, a.rs) != min(b.ls, b.rs)) {
			return min(a.ls, a.rs) > min(b.ls, b.rs);
		}
		if (max(a.ls, a.rs) != max(b.ls, b.rs)) {
			return max(a.ls, a.rs) > max(b.ls, b.rs);
		}
		return a.i < b.i;
	}
};
bool has[N];
LR lr[N];
int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int t; read(t);
	REP (icase, t) {
		int n, k; read(n, k);
		REP (i, n) has[i] = false;
		REP (i, n) lr[i].i = i;
		REP (i, k) {
			int l = -1;
			REP (j, n) {
				if (has[j]) l = j;
				lr[j].ls = j - l;
			}
			int r = n;
			DWN (j, n) {
				if (has[j]) r = j;
				lr[j].rs = r - j;
			}
			LR p = lr[0];
			REP (j, n) {
				p = min(p, lr[j]);
			}
			has[p.i] = true;
			if (i == k - 1) {
				int x = max(p.ls, p.rs) - 1;
				int y = min(p.ls, p.rs) - 1;
				printf("Case #%d: %d %d\n", icase + 1, x, y);
			}
		}
	}
	return 0;
}

