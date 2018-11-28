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

#define ull unsigned long long
#define ll long long
#define lson l,mid,id<<1
#define rson mid+1,r,id<<1|1

typedef pair<int, int>pii;
typedef pair<ll, ll>pll;
typedef pair<double, double>pdd;
const double eps = 1e-6;
const int MAXN = 100005;
const int MAXM = 5005;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int INF = 0x3f3f3f3f;
const double FINF = 1e18;
const ll MOD = 1000000007;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	string s;
	int t, cas = 0, pos, k, ans;
	scanf("%d", &t);
	while (t--)
	{
		ans = 0;
		cin >> s >> k;
		if (s.size() < k)
		{
			printf("Case #%d: ", ++cas);
			bool flag = 1;
			for (int i = 0; i < s.size() && flag; ++i)
			{
				if (s[i] == '-')flag = 0;
			}
			if (flag == 0)printf("IMPOSSIBLE\n");
			else
			{
				printf("%d\n", ans);
			}
		}
		else
		{
			for (int i = 0; i <= s.size() - k; ++i)
			{
				if (s[i] == '-')
				{
					ans++;
					for (int u = i; u <= i + k - 1; ++u)
					{
						if (s[u] == '-')s[u] = '+';
						else s[u] = '-';
					}
				}
			}
			printf("Case #%d: ", ++cas);
			bool flag = 1;
			for (int i = 0; i < s.size() && flag; ++i)
			{
				if (s[i] == '-')flag = 0;
			}
			if (flag == 0)printf("IMPOSSIBLE\n");
			else
			{
				printf("%d\n", ans);
			}
		}
	}
}