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

const int MAXN = 1e4;
const int SQRTN = 550;
const int LOGN = 60;
const int INT_INFINITY = 1001001001;
const int LIMIT = 1e6;

const slong LONG_INFINITY = 1001001001001001001ll;
const slong LONG_LIMIT = 200100100100101ll;

slong n, k;

pair<slong, slong> getMinMax(slong length, slong n)
{
	assert(n <= length);
	
	if (n == length)
	{
		return {0, 0};
	}
	
	if (n == 1)
	{
		if (length % 2)
		{
			return mp(length/2, length/2);
		}
		else
		{
			return mp(length/2-1, length/2);
		}
	}
	else
	{
		n--;
		
		if (n == 1)
		{
			slong newlen = length/2;
			if (newlen % 2)
			{
				return mp(newlen/2, newlen/2);
			}
			else
			{
				return mp(newlen/2-1, newlen/2);
			}
		}
		
		slong small = n/2;
		slong big = n - small;
		
		if (length % 2)
		{
			return getMinMax(length/2, big);
		}
		else
		{
			pair<slong, slong> curr = {-1, -1};
			if (small == big)
			{
				curr = max(curr, getMinMax(length/2 - 1, big));
			}
			else
			{			
				curr = max(curr, min(getMinMax(length/2, big), getMinMax(length/2 - 1, small)));
			}
			
			return curr;
		}
	}
}

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
		cin >> n >> k;
		auto x = getMinMax(n, k);
		
		assert(x.fi != -1);
		assert(x.se != -1);
		
		cout << "Case #" << t << ": " << x.se << " " << x.fi << endl;
	}
	
	return 0;
}
