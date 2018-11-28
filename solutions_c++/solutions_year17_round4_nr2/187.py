#include <iostream>
#include <thread>
#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <unistd.h>
#include <cmath>
#include <set>
#include <queue>

using namespace std;

typedef long long ll;
typedef double dd;
const ll size = 111002;
const ll mod = 1000000007;
#define P(a) cout<<(a)<<endl;
#define PP(a) cout<<(a)<<' ';
#define FOR(i, a, b)   for (int i = (a); i <= (b); ++i)
#define FORD(i, a, b)  for (int i = (a); i >= (b); --i)
#define REP(i, b)      for (int i =  0 ; i <  (b); ++i)
#define mid ((l+r)/2)
#define lp (p*2)
#define rp (p*2+1)
void PLL(initializer_list<ll> li) {
	for (auto beg = li.begin(); beg != li.end(); beg++) {
		if (beg != li.begin()) cout << ' '; cout << *beg;
	} cout << endl;
}

int t, n, m, cnt[1111], num[1111], c;

int main () {
	cin >> t;
	for (int ca = 1; ca <= t; ca++) {
		cin >> n >> c >> m;
		memset(cnt, 0, sizeof(cnt));
		memset(num, 0, sizeof(num));
		int ans = 0, ans2 = 0;
		while (m--) {
			int a, b;
			cin >> a >> b;
			ans = max(ans, ++num[b]);
			cnt[a]++;
		}
		int tot = 0;
		FOR(i, 1, n) {
			tot += cnt[i];
			while (tot > ans * i) ans++;
		}
		FOR(i, 1, n) {
			if (ans < cnt[i]) ans2 += cnt[i]-ans;
		}

		printf("Case #%d: %d %d\n", ca, ans, ans2);
	}
}
