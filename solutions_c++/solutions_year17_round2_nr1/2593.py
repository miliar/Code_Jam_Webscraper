//Created By Mayur Agarwal :)

#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <algorithm>
#include <map>
#include <iterator>
#include <functional>
#include <queue>
#include <stack>
#include <iomanip>

#define ll long long
#define ind(a) scanf("%d",&a)
#define in(a) scanf("%lld",&a)
#define inc(a) scanf("%c",&a)
#define ins(a) scanf("%s",a)
#define pr(a) printf("%lld\n",a)
#define bitcnt(x) __builtin_popcountll(x)
#define debug(x) cout << #x << " = " << x << endl
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define pb push_back
#define MP make_pair
#define ff first
#define ss second
#define SIZE 200010
const ll mod = 1000000007L;

using namespace std;
typedef pair<ll, ll>pll;
typedef long double ld;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		int n;
		ll d;
		cin >> d >> n;
		ld max_tim = 0;
		for (int i = 0; i < n; i++)
		{
			ld k, s;
			cin >> k >> s;
			ld temp = ((d - k) * 1.0) / (s * 1.0);
			max_tim = max(max_tim, temp);
		}
		//cout << max_tim << endl;
		ld ans = (d * 1.0) / max_tim;
		cout << "Case #" << tc << ": " << fixed << setprecision(7) << ans << endl;
	}
	return 0;
}