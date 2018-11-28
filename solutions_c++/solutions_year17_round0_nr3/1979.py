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

ll n, k;
map<ll, ll, greater<ll> > mp;

int main() {
//	freopen("C-large.in", "rt", stdin);
//	freopen("out.txt", "wt", stdout);
	int t; scanf("%d", &t);
	FOR(kase, 1, t) {
		scanf("%lld%lld", &n, &k);
		mp.clear();
		printf("Case #%d: ", kase);
		mp[n] = 1;
		while (1) {
			if (!SZ(mp)) break;
			map<ll, ll, greater<ll> >::iterator it = mp.begin();
			if (k <= it->second) {
				ll tmpl = it->first;
				printf("%lld ", tmpl / 2LL);
				if (tmpl % 2LL == 0LL) printf("%lld", (tmpl / 2LL) - 1);
				else printf("%lld", tmpl / 2LL);
				break;
			} else {
				k -= it->second;
				ll tmpl = it->first;
				if (tmpl % 2LL) mp[tmpl / 2LL] += 2LL*it->second;
				else mp[tmpl / 2LL] += it->second, mp[(tmpl / 2LL) - 1] += it->second;
				mp.erase(mp.begin());
			}
		}
		printf("\n");
	}
	return 0;
}
