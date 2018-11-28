#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <cmath>
#include <vector>
#include <deque>
#include <functional>
#include <iterator>
#include <utility>
#include <bitset>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <cctype>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;

#define FOR(i, a, b) for(int i = (a); i <= (b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a) - 1; i >= (b); --i)
#define SZ(x) ((int)x.size())
#define openfile {freopen("inp.txt","rt",stdin);freopen("out.txt","wt",stdout);}
#define debug 0

template <typename T> inline void next_int(T &x) {
	x = 0; char c; bool neg = false;
	while (!isdigit(c = getchar())) if (c == '-') neg = true;
	do x = x*10 + c - 48; while (isdigit(c = getchar()));
	if (neg) x = -x;
}

template <typename T> inline void write_int(T x, char last = 0) {
	if (x < 0) putchar('-'), x = abs(x);
	char tmp[20]; int cnt = 0;
	while (x >= 10) tmp[cnt++] = x % 10 + 48, x /= 10;
	tmp[cnt] = x + 48;
	FORD(i, cnt, 0) putchar(tmp[i]);
	if (last) putchar(last);
}

ull n, num[19], pw[19];
char sn[19];

ull solve() {
	int cnt = 0; ull x = n;
	while (x > 0) sn[++cnt] = x % 10ULL, x /= 10ULL;
	reverse(sn + 1, sn + cnt + 1);
	ull ret = 0, pref = 0;
	FOR(i, 1, cnt) {
		if (i == 1 || (i > 1 && sn[i] >= sn[i - 1])) {
			ull tmppref = 0;
			if ((i == 1 && sn[i] > 1) || (i > 1 && sn[i] > 0)) {
				if (i == 1 || (i > 1 && sn[i] > sn[i - 1])) {
					tmppref = pref * 10ULL + (ull)(sn[i] - 1);
					ret = max(ret, tmppref * pw[cnt - i] + num[cnt - i]);
				}
			}
			tmppref = pref * 10ULL + (ull)sn[i];
			ull tmpx = tmppref * pw[cnt - i] + num[cnt - i];
			if (tmpx <= n) ret = max(ret, tmpx);
			pref = pref * 10ULL + (ull)sn[i];
		} else break;
	}
	return ret;
}

int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	pw[0] = 1;
	FOR(i, 1, 18) num[i] = num[i - 1] * 10ULL + 9ULL, pw[i] = pw[i - 1] * 10ULL;
	int t; scanf("%d", &t);
	FOR(kase, 1, t) {
		scanf("%llu", &n);
		printf("Case #%d: ", kase);
		ull tmp = 0;
		FOR(i, 1, 18) {
			if (num[i] > n) break;
			tmp = num[i];
		}
		if (tmp == n) printf("%llu\n", tmp);
		else printf("%llu\n", max(tmp, solve()));
	}
	return 0;
}
