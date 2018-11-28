#include<bits/stdc++.h>
#include <math.h>
using namespace std;
typedef long long int ll;
typedef long double ld;
typedef pair<ld, ld> P;
#define _USE_MATH_DEFINES
#define mp make_pair
#define pb push_back
#define N 1003
long double dp[N][N], res, pi = 3.14159265358979323846;
P p[N];
int n, k, t, x, y, g = 0, ti[N][N];
bool comp(P d1, P d2)
{
	if (d1.first != d2.first)return d1.first > d2.first;
	return d1.second > d2.second;
}
ld solve(int pos, int ta)
{
	if (ta == k || pos >= n)return 0.0;
	ld c1, c2, &ans=dp[pos][ta];
	if (ti[pos][ta] == g)return ans;
	c1 = solve(pos + 1, ta + 1) + (2.0 * p[pos].second * p[pos].first * pi);
	c2 = solve(pos + 1, ta);
	if (ta == 0)c1 += (p[pos].first*p[pos].first* pi);
	ti[pos][ta] = g;
	return ans = max(c1, c2);
}
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	cout.precision(20);
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++)
			scanf("%d%d", &x, &y), p[i] = mp(double(x), double(y));//first -> radius
		g++;
		sort(p, p + n, comp);
		res = solve(0, 0);
		cout << "Case #" << g <<": " << res << "\n";
	}
	return 0;
}