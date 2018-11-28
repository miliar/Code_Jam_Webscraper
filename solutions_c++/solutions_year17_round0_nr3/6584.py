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
	freopen("C-small-1-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int  t,tt;
	cin >> t;
	tt = t;

	while (t--) {
		deque<pair<pair<ll, ll>, ll>> q;
		ll n, k;
		//cin >> n >> k;
		gtll(n);
		gtll(k);
		ll i=1,j=n;
		q.push_back(make_pair(make_pair(1, n),n-1));
		ll u = 0;
		ll b = 0;
		//k++;
		int flag = 0;
		if (n==k) {
			printf("Case #%d: 0 0\n", tt - t);
			continue;
		}
		while (k--) {
			flag = 0;
			sort(q.begin(), q.end(), sortbys);
			 i = q.front().first.first;
			 j = q.front().first.second;
			q.pop_front();
			bool f = false;
			if ((j - i + 1) % 2 == 0) {
				u = (j - i + 1) / 2;
				f = true;
			}
			else
				u = ((j - i + 1) / 2)+1;

			if (f) {
				if (j >= i + u) {
					q.push_back(make_pair(make_pair(i + u, j),j-i-u));
					flag++;
				}
				if (j - u - 1 >= i) {
					q.push_back(make_pair(make_pair(i, j - u - 1),j-u-1-i));
					flag++;
				}
			}
			else {
				if (j - u >= i) {
					q.push_back(make_pair(make_pair(i, j - u),j-u-i));
					flag++;
				}
				if (j >= i + u) {
					q.push_back(make_pair(make_pair(i + u, j),j-i-u));
					flag++;
				}
			}

			
			
		}
		if (q.empty()) {
			printf("Case #%d: 0 0\n", tt - t);
		}
		else if (flag==1) {
			i = q.back().first.first;
			j = q.back().first.second;
			q.pop_back();
			u = (j - i + 1);
			printf("Case #%d: %lld 0\n", tt - t, u);
		}
		else if (flag == 2) {
			i = q.back().first.first;
			j = q.back().first.second;
			q.pop_back();
			
			u = (j - i + 1);

			i = q.back().first.first;
			j = q.back().first.second;
			q.pop_back();
			b = (j - i + 1);
			printf("Case #%d: %lld %lld\n", tt - t, max(u, b), min(b, u));
		}
		else{
			printf("Case #%d: 0 0\n", tt - t);
		}
		//cout << "Case #" << tt - t << ":" << " "<<ans << endl;
		
	}


	return 0;
}