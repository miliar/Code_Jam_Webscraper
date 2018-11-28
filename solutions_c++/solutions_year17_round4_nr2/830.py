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

const int MAXN = 1000;
const int SQRTN = 550;
const int LOGN = 60;
const int INT_INFINITY = 1001001001;
const int LIMIT = 1e6;

const slong LONG_INFINITY = 1001001001001001001ll;
const slong LONG_LIMIT = 200100100100101ll;

const double DOUBLE_INFINITY = 1e16;

int n, c, m;
int countPlayer[MAXN+5];
int atPosition[MAXN+5];
bool currentTaken[MAXN+5];
//vector<int> atPosition[MAXN+5];

int main()
{
	#ifdef VSP4
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
	
	cout.tie(0);
	cin.tie(0);
	
	int t, T, i, j, p, b;
	
    cin >> T;
	
    for (t = 1; t <= T; t++)
	{
		cin >> n >> c >> m;
		
		memset(countPlayer, 0, sizeof(countPlayer));
		memset(atPosition, 0, sizeof(atPosition));
		
		/*
		for (i = 1; i <= n; i++)
		{
			atPosition[i].clear();
		}
		*/
		
		vector<pair<pii, bool> > data;
		
		for (i = 1; i <= m; i++)
		{
			cin >> p >> b;
			data.eb(mp(p, b), false);
			countPlayer[b]++;
			atPosition[p]++;
		}
		
		sort(ALL(data));
		
		int trips = 0;
		
		while (true)
		{
			int last = 0;
			
			memset(currentTaken, false, sizeof(currentTaken));
			
			for (auto &s: data)
			{
				if (!s.se)
				{
					if (!currentTaken[s.fi.se] && s.fi.fi > last)
					{
						currentTaken[s.fi.se] = true;
						last++;
						s.se = true;
					}
				}
			}
			
			if (last == 0)
			{
				break;
			}
			
			trips++;
		}
		
		for (i = 1; i <= c; i++)
		{
			assert(trips >= countPlayer[i]);
		}
		
		int promotions = 0;
		
		queue<int> positionsLeft;
		
		for (i = 1; i <= n; i++)
		{
			if (atPosition[i] <= trips)
			{
				int left = trips - atPosition[i];
				for (j = 0; j < left; j++)
				{
					positionsLeft.push(i);
				}
			}
			else
			{
				int pros = atPosition[i] - trips;
				promotions += pros;
				
				/*
				for (j = 0; j < pros; j++)
				{
					positionsLeft.push(i);
				}
				*/
				
				for (j = 0; j < pros; j++)
				{
					assert(!positionsLeft.empty());
					assert(positionsLeft.front() < i);
					positionsLeft.pop();
				}
			}
		}
		
		cout << "Case #" << t << ": " << trips << " " << promotions << endl;
	}
	
	return 0;
}
