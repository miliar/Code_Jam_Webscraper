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
	return((a.second<b.second));
}

//bitset<10> bs;
//map<ll, ll> skew;
//ll mat[1002][1002];
//freopen("input.txt", "rt", stdin);
//freopen("output.txt", "wt", stdout);
//stack<string> st;
//vector<pair<pair<ll, ll>, ll>>v;
//vector<ll>vf;



//bool happy(string s) {
//	for (int i = 0;i < s.size();i++) {
//		if (s[i] != '+')
//			return false;
//	}
//	return true;
//}
string flip(string s, int u,int k) {
	
	for (int i = u;i < u+k;i++) {
		if (s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	}
	return s;
}


int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int  t,tt;
	cin >> t;
	tt = t;

	while (t--) {
		string s;
		int k;
		cin >> s>>k;
		int flag = 1;
		int ans = 0;
		for (int i = 0;i < s.size();i++) {
			if (s[i] == '-' && (s.size() - i) < k)
				flag = 2;
			else if (s[i] == '-') {
				s = flip(s, i, k);
				ans++;
			}

		}
		if(flag==2)
		    cout << "Case #" << tt - t << ":" << " IMPOSSIBLE" << endl;
		else
			cout << "Case #" << tt - t << ":" << " "<<ans << endl;
	}


	return 0;
}