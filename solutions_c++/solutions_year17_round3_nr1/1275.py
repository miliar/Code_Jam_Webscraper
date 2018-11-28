/*
B name oooo
ID: amin_un1
PROG: ride
LANG: C++

my ID
uva = "sir sbu"
codforsec = "sir_sbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <cmath>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <bitset>
#include <complex>
#include <iomanip>
#include <time.h>
using namespace std;

#define ll long long
#define ld long double

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAX = 100001;
const long long mod = 1000 * 1000 * 1000 + 7;

#define mp make_pair
#define pb(a) push_back(a)
#define L(s) (int)((s).size())
#define all(c) (c).begin(), (c).end()

#define INF (1e9)
#define EPS (1e-9)
#define E (2.718281828459045)
#define P (3.14159265358979323846)


////////////////////////////////////////////////////code///////////////////////////////////////
int  n, k;

vector<pair<ll, ll> >vec;
double dp[1000 + 10][1000 + 10];


double f(ll r1 , ll r2 , ll h1)
{
	double ans = r1 * 2ll * P*h1;
	ans += (r1*r1-r2*r2)*P;
	return ans;
}

double get(int a, int b , int index )
{
	if (b == k)
	{
		return 0;
	}
	if(index == n + 1)
	{
		return -1000000000000000;
	}

	if (dp[a][b] >= 0)
		return dp[a][b];
	double ans = get(index, b + 1, index + 1) + f(vec[index].first, vec[a].first, vec[index].second);
	double ans1 = get(a, b, index + 1);
	return dp[a][b] = max(ans, ans1);
}
int main()
{
	//ofstream cout ("test.out");
	//ifstream cin ("test.in");
	freopen("AA.txt" ,"r" , stdin);
	freopen( "AAAaoutput.txt" , "w" , stdout );

	int t = 0; 
	cin >> t;
	int test = 1;
	while(t -- )
	{
		cin >> n >> k;
		double ans = 0.0;
		vec.clear();
		memset(dp, -1, sizeof dp);
		pair<ll, ll> z;
		z.first = 0;
		z.second = 0;
		vec.push_back(z);
		for(int i = 0 ; i < n ; i ++)
		{
			ll r, h;
			cin >> r >> h;
			pair<ll, ll> a;
			a.second = h;
			a.first = r;
			vec.push_back(a);

		}
		sort(all(vec));
		
		ans = get(0, 0, 1);
		/*for(int i = 0 ; i < k ; i ++)
		{
			int r2 = 0;
			if(i != k-1)
			{
				r2 = vec[i + 1].first;
			}
			ans += f(vec[i].first, r2, vec[i].second);
		}*/
		printf("Case #%d: %.9f\n", test++ , ans);
	}
}

