#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define cint(d) scanf("%d", &d)
#define cint2(a, b) scanf("%d %d", &a, &b)
#define cint3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define cint4(a, b, c, d) scanf("%d %d %d %d", &a, &b, &c, &d)

#define clong(d) scanf("%lld", &d)
#define clong2(a, b) scanf("%lld %lld", &a, &b)
#define clong3(a, b, c) scanf("%lld %lld %lld", &a, &b, &c)
#define clong4(a, b, c, d) scanf("%lld %lld %lld %lld", &a, &b, &c, &d)

#define foreach(v, c) for(__typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define revforeach(v, c) for(__typeof( (c).rbegin()) v = (c).rbegin();  v != (c).rend(); ++v)
#define ALL(v) (v).begin(), (v).end()

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second

typedef long long int slong;
typedef pair<int, int> pii;
typedef pair<slong, slong> pll;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

#ifdef VSP4 
    #include "debug.h"    
#else
    #define debug(args...)                  // Just strip off all debug tokens
#endif

const int MOD = 1000000007;
#define MODSET(d) if ((d) >= MOD) d %= MOD;
#define MODNEGSET(d) if ((d) < 0) d = ((d % MOD) + MOD) % MOD;
#define MODADDSET(d) if ((d) >= MOD) d -= MOD;
#define MODADDWHILESET(d) while ((d) >= MOD) d -= MOD;

const int MAXN = 100;
const int SQRTN = 550;
const int LOGN = 60;
const int INT_INFINITY = 1001001001;
const int LIMIT = 1e6;

const slong LONG_INFINITY = 1001001001001001001ll;
const slong LONG_LIMIT = 200100100100101ll;

const double DOUBLE_INFINITY = 1e16;

int n, p;
int arr[MAXN+5];

int main()
{
	#ifdef VSP4
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
	
	cout.tie(0);
	cin.tie(0);
	
	int t, T, i, j;
	
	vector<tuple<int, int, int> > data;
	
    cin >> T;
	
    for (t = 1; t <= T; t++)
	{
		cin >> n >> p;
		
		for (i = 1; i <= n; i++)
		{
			cin >> arr[i];
		}
		
		int ans = 0;
		
		if (p == 2)
		{
			int even = 0;
			int odd = 0;
			
			for (i = 1; i <= n; i++)
			{
				if (arr[i] % 2)
				{
					odd++;
				}
				else
				{
					even++;
				}
			}
			
			ans = even + (odd+1)/2;			
		}
		else if (p == 3)
		{
			int cnt[3];
			cnt[0] = cnt[1] = cnt[2] = 0;
			
			for (i = 1; i <= n; i++)
			{
				cnt[arr[i] % 3]++;
			}
			
			ans = cnt[0];
			
			while (cnt[1] && cnt[2])
			{
				cnt[1]--;
				cnt[2]--;
				ans++;
			}
			
			while (cnt[1] >= 3)
			{
				cnt[1] -= 3;
				ans++;
			}
			
			while (cnt[2] >= 3)
			{
				cnt[2] -= 3;
				ans++;
			}
			
			if (cnt[1] || cnt[2])
			{
				ans++;
			}
		}
		else if (p == 4)
		{
			int cnt[4];
			cnt[0] = cnt[1] = cnt[2] = cnt[3] = 0;
			
			for (i = 1; i <= n; i++)
			{
				cnt[arr[i] % 4]++;
			}
			
			for (int i = 0; i <= n; i++)
			{
				for (int j = 0; j <= n; j++)
				{
					for (int k = 0; k <= n; k++)
					{
						/*
						 * 
0 1 2
1 0 1
2 1 0
*/

						int cntone = j*1 + k*2;
						int cnttwo = i*1 + k*1;
						int cntthree = 2*i + j*1;
						
						if (cntone <= cnt[1] && cnttwo <= cnt[2] && cntthree <= cnt[3])
						{
							int temp = i + j + k;
							temp += cnt[0];
							
							/*
							 * 0 0 4
4 0 0
0 2 0
*/

							int left3 = cnt[3] - cntthree;
							int onlythree = left3/4;
							int newleftthree = left3 % 4;							
							temp += onlythree;
							
							int left2 = cnt[2] - cnttwo;
							int onlytwo = left2/2;
							int newlefttwo = left2 % 2;							
							temp += onlytwo;
							
							int left1 = cnt[1] - cntone;
							int onlyone = left1/4;
							int newleftone = left1 % 4;							
							temp += onlyone;
							
							if (newleftone || newlefttwo || newleftthree)
							{
								temp++;
							}
							
							ans = max(ans, temp);
						}
					}
				}
			}
		}
		else
		{
			assert(false);
		}
		
		assert(ans <= n);
		
		cout << "Case #" << t << ": " << ans << endl;
	}
	
	return 0;
}
