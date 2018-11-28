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
#include<unordered_set>
#include<unordered_map>
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
const int MAXN = 100005;
const int MAXM = 5005;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int INF = 0x3f3f3f3f;
const double FINF = 1e18;
const ll MOD = 1000000007;
const double PI = acos(-1);

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, cas = 0, n, m;
	scanf("%d", &T);
	string a[105];
	while(T--)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) 
		{
			cin >> a[i];
			for (int j = 0; j < m; j++) 
			{
				if (a[i][j] != '?') 
				{
					for (int k = j - 1; k >= 0; k--) 
					{
						if (a[i][k] != '?')break;
						a[i][k] = a[i][j];
					}
					for (int k = j + 1; k < m; k++) 
					{
						if (a[i][k] != '?') break;
						a[i][k] = a[i][j];
					}
				}
			}
		}
		for (int i = 0; i < n; i++) 
		{
			if (a[i][0] != '?') 
			{
				for (int j = i - 1; j >= 0; j--) 
				{
					if (a[j][0] != '?')break;
					a[j] = a[i];
				}
				for (int j = i + 1; j < n ; j++) 
				{
					if (a[j][0] != '?')break;
					a[j] = a[i];
				}
			}
		}
		printf("Case #%d:\n", ++cas);
		for (int i = 0; i < n; ++i)cout << a[i] << endl;
	}
}
