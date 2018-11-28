#include<iostream>
#include<cstdio>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cstring>
#include<string>
#include<vector>
#include<iomanip>
//#include<unordered_set>
//#include<unordered_map>
#include<cmath>
#include<list>
#include<bitset>
using namespace std;
#define _____ ios::sync_with_stdio(false); cin.tie(0);
#define ull unsigned long long
#define ll long long
#define lson l,mid,id<<1
#define rson mid+1,r,id<<1|1

typedef pair<int, int>pii;
typedef pair<ll, ll>pll;
typedef pair<double, double>pdd;
const double eps = 1e-6;
const int MAXN = 10005;
const int MAXM = 5005;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int INF = 0x3f3f3f3f;
const double FINF = 10000000;
const ll MOD = 123456789;
const double PI = acos(-1);
double p[105];
int t, n, k, cas = 0; double sum;
bool judge(double tmp)
{
	double all = 0;
	for (int i = 0; i < n; ++i)
	{
		all += max(0.0, tmp - p[i]);
	}
	if (all > sum)return false;
	else return true;
}
int main()
{
	freopen("C-small-1-attempt2.in", "r", stdin);
	freopen("C-small-1-attempt2.out", "w", stdout);
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d%d", &n, &k);
		scanf("%lf", &sum);
		for (int i = 0; i < n; ++i)scanf("%lf", &p[i]);
		double l = 0, r = 1, mid;
		while (l < r)
		{
			if (r - l < 1e-10)break;
			mid = (l + r) / 2;
			if (judge(mid))l = mid;
			else r = mid;
		}
		double ans = 1;
		for (int i = 0; i < n; ++i)ans *= max(l, p[i]);
		printf("Case #%d: %.10lf\n", ++cas, ans);
	}
}