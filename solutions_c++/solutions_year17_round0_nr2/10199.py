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

char str[20];
char ans[20];
int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t; read(t);
	REP (icase, t) {
		read(str);
		int n = strlen(str);
		int p = n;
		REP (i, n - 1) {
			if (str[i] > str[i + 1]) {
				p = i;
				break;
			}
		}
		if (p == n) {
			printf("Case #%d: %s\n", icase + 1, str);
		} else {
			int i = 0;
			while (i >= 0 && str[i] == str[p]) i--; i++;
			for (int j = 0; j < i; j++) {
				ans[j] = str[j];
			}
			ans[i] = str[i] - 1;
			for (int j = i + 1; j < n; j++) {
				ans[j] = '9';
			}
			ans[n] = 0;
			printf("Case #%d: %s\n", icase + 1, ans[0] == '0' ? ans + 1 : ans);
		}
	}
	return 0;
}

