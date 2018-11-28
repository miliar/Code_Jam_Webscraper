#include<bits/tdc++.h>
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
const int MAXN = 100005;
const int MAXM = 5005;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int INF = 0x3f3f3f3f;
const double FINF = 1e18;
const ll MOD = 1000000007;
const double PI = acos(-1);
int a[105];
int b[105][105];
int h[105];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, cas = 0,ans;
	scanf("%d", &T);
	while(T--)
	{
		ans = 0;
		memset(h, 0, sizeof(h));
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)scanf("%d", &a[i]);
		for (int i = 0; i < n; i++) 
		{
			for (int j = 0; j < m; j++) 
			{
				scanf("%d", &b[i][j]);
			}
			sort(b[i], b[i] + m);
		}
		int flag = 0;
		for (int z = 0;flag!=-1; z++) 
		{
			flag = 1;
			for (int i = 0; i < n; i++) 
			{
				while (h[i] < m && b[i][h[i]] * 10 < a[i] * z * 9) h[i]++;
				if (h[i] == m) 
				{
					flag = -1;
					break;
				}
				if (b[i][h[i]] * 10 > a[i] * z * 11) 
				{
					flag = 0;
					break;
				}
			}
			if (flag == 1) 
			{
				ans++;
				for(int i = 0;i < n; ++i)
				{
					h[i]++;
				}
				z--;
			}
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}
