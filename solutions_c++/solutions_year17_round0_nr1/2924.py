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
		int k;
		scanf("%s %d", buff, &k);
		string s(buff);
		int cnt = 0;
		for (int i = 0; i + k - 1 < sz(s); i++){
			if (s[i] != '+'){
				cnt++;
				for (int j = 0; j < k; j++)
					s[i + j] = (s[i + j] == '+' ? '-' : '+');
			}
		}
		bool isOk = true;
		for (int i = 0; i < sz(s); i++){
			if (s[i] == '-')
				isOk = false;
		}
		printf("Case #%d: ", tt + 1);
		if (isOk) printf("%d\n", cnt);
		else puts("IMPOSSIBLE");
	}
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
	return 0;
}