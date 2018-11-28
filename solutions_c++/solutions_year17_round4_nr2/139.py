/*
ЗАПУСКАЕМ
░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
▄███▀░◐░░░▌░░░░░░░
░░░░▌░░░░░▐░░░░░░░
░░░░▐░░░░░▐░░░░░░░
░░░░▌░░░░░▐▄▄░░░░░
░░░░▌░░░░▄▀▒▒▀▀▀▀▄
░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░▄▄▌▌▄▌▌░░░░░ 
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define zhfs main
#define mp(a, b) make_pair(a, b)
#define fi first
#define se second
#define re return
#define forn(i, n) for (int i = 1; i <= n; i++)
const int MAXN = 1007;
vector<int> onPos[MAXN], onMan[MAXN];
int b[MAXN], p[MAXN];
int size[MAXN];
int zhfs()
{
#ifdef LOCAL
//	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		for (int i = 0; i < MAXN; i++)
		{
			onPos[i].clear();
			onMan[i].clear();
		}
		int n, c, m;
		scanf("%d %d %d", &n, &c, &m);
		for (int i = 1; i <= m; i++)
		{
			scanf("%d %d", &p[i], &b[i]);
			onPos[p[i]].push_back(i);
			onMan[b[i]].push_back(i);
		}
		int res = 0;
		for (int i = 1; i <= c; i++)
		{
			res = max(res, (int)onMan[i].size());
		}
		int sum = 0;
		for (int i = 1; i <= n; i++)
		{
			sum += (int)onPos[i].size();
			res = max(res, (sum + i - 1) / i);
		}
		int ans = 0;
		for (int i = 1; i <= n; i++)
		{
			int more = (int)onPos[i].size() - res;
			if (more > 0) ans += more;
		}
		printf("Case #%d: %d %d\n", tt, res, ans);
	}

}

