
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>
using namespace std;
using ll = long long;

//Solution C for small 1,2 and large
int main(void)
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		ll n, k;
		cin >> n >> k;
		ll cone = n;
		ll a = 1, b = 0;
		ll pas = 0;
		ll ans = -1;
		for (;;)
		{
			ll na = (cone % 2) ? (a + a + b) : a;
			ll nb = (cone % 2) ? b : (a + b + b);
			ll ncon = (cone % 2) ? (cone / 2) : (cone / 2 - 1);
			if (pas + b >= k)
			{
				ans = cone + 1;
				break;
			}
			pas += b;
			if (pas + a >= k)
			{
				ans = cone;
				break;
			}
			pas += a;
			a = na; b = nb;
			cone = ncon;
		}
		cout << "Case #" << test + 1 << ": ";
		ll big = (ans % 2) ? (ans - 1) / 2 : ans / 2;
		ll sml = (ans % 2) ? (ans - 1) / 2 : ans / 2 - 1;
		cout << big << " " << sml << endl;
	}
	return 0;
}
