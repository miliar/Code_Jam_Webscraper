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

const int MAXN = 50;
const int SQRTN = 550;
const int LOGN = 60;
const int INT_INFINITY = 1001001001;
const int LIMIT = 1e6;

const slong LONG_INFINITY = 1001001001001001001ll;
const slong LONG_LIMIT = 200100100100101ll;

int N, P;
int req[MAXN+5];
int amount[MAXN+5][MAXN+5];

int memo[10][(1 << 10)];

const int TRY = 1000;

bool marked[100][100];

int main()
{
	#ifdef VSP4
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
	
	cout.tie(0);
	cin.tie(0);
	
	int t, T, i, j;
	
    cin >> T;
	
    for (t = 1; t <= T; t++)
	{
		cin >> N >> P;
		
		for (i = 0; i < N; i++)
		{
			cin >> req[i];
		}
		
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < P; j++)
			{
				cin >> amount[i][j];
			}
			sort(amount[i], amount[i] + P, greater<int>());
			
			/*
			for (j = 0; j < P; j++)
			{
				cout << amount[i][j] << " ";
			}
			cout << endl;
			*/
			
		}
		
		memset(marked, false, sizeof(marked));
		
		int ans = 0;
		
		for (int nowmake = 2000000; nowmake >= 1; nowmake--)
		{
			int lastval = P;
			
			for (i = 0; i < N; i++)
			{
				int curr = 0;
				
				for (j = 0; j < P; j++)
				{
					if (!marked[i][j])
					{
						slong reqvolume = 1ll*nowmake*req[i];
						slong currentvolume = amount[i][j];
						
						if ((10*currentvolume >= 9*reqvolume) && (10*currentvolume <= 11*reqvolume))
						{
							curr++;
						}
					}
				}
				
				lastval = min(lastval, curr);
				
				if (lastval == 0)
				{
					break;
				}
				
			}
			
			if (lastval)
			{
				ans += lastval;
				
				for (i = 0; i < N; i++)
				{
					int curr = lastval;
					
					for (j = 0; j < P; j++)
					{
						if (!marked[i][j])
						{
							slong reqvolume = 1ll*nowmake*req[i];
							slong currentvolume = amount[i][j];
							
							if ((10*currentvolume >= 9*reqvolume) && (10*currentvolume <= 11*reqvolume))
							{
								marked[i][j] = true;
								curr--;
								if (curr == 0)
								{
									break;
								}
							}
						}
					}
				}
			}
		}
		
		{
			cout << "Case #" << t << ": " << ans << endl;
		}
	
		
	}
	
	return 0;
}
