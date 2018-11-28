#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include <stdio.h>
#include <string.h>
#include<string>
#include <vector>
#include <bitset>
#include<iomanip>
#include<algorithm>
#include <utility> 
#include<cmath>
#include<stack>
#include<queue>
#include <deque>
#include<list>
#include<set>
#include<map>
#include<ctime>
#include<sstream>
#include <iterator>
#include<functional>

template<typename T>
inline T gcd(T a, T b) { T c;while (b) { c = b;b = a % b;a = c; }return a; }
template< typename T>
T lcm(T a, T b) { return b*(a / gcd(a, b)); }
template< typename T>
inline T pow2(T base, T n)
{
	T ansp = 1;
	while (n)
	{
		if (n & 1)
			ansp *= base;
		n >>= 1;
		base *= base;
	}

	return ansp;
}
//#define loop(i, j , n) for(long long i=j; i<n; i++)
#define ll long long
#define ld long double
#define gtld(t) scanf("%ld",&t)
#define gtll(f) scanf("%lld",&f)
#define gts(g) scanf("%s",&g)
#define gti(k) scanf("%d",&k)
#define gtch(ch) scanf(" %c", &ch)
#define eb emplace_back
using namespace std;
bool sortbys(const pair<pair<ll, ll>, ll> &a, const pair<pair<ll, ll>, ll> &b)
{
	return((a.second>b.second));
}

//bitset<10> bs;
//map<ll, ll> skew;
//ll mat[1002][1002];
//freopen("input.txt", "rt", stdin);
//freopen("output.txt", "wt", stdout);
//stack<string> st;
//vector<pair<pair<ll, ll>, ll>>v;
//vector<ll>vf;


int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int  t,tt;
	cin >> t;
	tt = t;

	while (t--) {
		ll d, n,x;
		
		gtll(d);
		gtll(n);
		ld tim =0.0, sp=0.0, ans = 0.0;
		for (ll i = 0;i < n;i++)
		{
			gtll(x);
			cin >> sp;
			tim = max(tim,(d - x) / sp);
			ans = d / tim;
		}
		
			printf("Case #%d: ", tt - t);
			cout <<fixed << setprecision(7) << ans << endl;
		
	
		
	}


	return 0;
}