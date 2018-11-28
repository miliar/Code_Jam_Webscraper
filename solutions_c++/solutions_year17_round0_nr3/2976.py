#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <list>
#include <set>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <ctime>
#include <queue>
#include <map>
#include <cstring>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef bool bl;
typedef pair<bl, bl> pbl;
typedef pair<ld, ld> pld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define mp make_pair
#define ft first
#define sd second
#define forn(i, y, x) for(int i = y; i < x; i++)
#define ford(i, y, x) for(int i = y; i >= x; i--)
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define error exit(1)
const ll mod = (ll)1e9 + 7;
const int inf = (int)2e9;
const ll INF = (ll)1e18;
const int base = 1000 * 1000 * 1000;
const int maxn = 2005;
const ld pi = acosl(-1.0);
const ld eps = 1e-9;

char buff[1234];

void solve()
{
	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		printf("Case #%d: ", tt + 1);

		ll n, k;
		scanf("%I64d %I64d", &n, &k);
		k--;
		ll j = 1;
		while ((1ll << j) - 1 <= k) j++;
		j--;
		j = (1ll << j) - 1;

		ll seg = j + 1;
		ll ost = n - j;
		ll a[] = { seg - ost % seg, ost % seg };
		k -= j;
		ll cnt = ost / seg + (a[1] > k ? 1 : 0);
		pll ans;
		if (cnt % 2) ans = mp((cnt - 1) / 2, (cnt - 1) / 2);
		else ans = mp(cnt / 2, cnt / 2 - 1);
		printf("%I64d %I64d\n", ans.ft, ans.sd);
	}
}

int main()
{
#ifdef _DEBUG
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
	return 0;
}