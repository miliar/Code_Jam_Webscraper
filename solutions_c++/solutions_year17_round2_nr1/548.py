/*
Hanit Banga
*/

#include <algorithm>
#include <iostream>
#include "iomanip"
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define fast_cin() ios_base::sync_with_stdio(false)

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int N = 1e3 + 5;

ll k[N], s[N];
double r[N];

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		ll d; int n;
		cin >> d >> n;
		for (int i = 0; i < n; ++i)
			cin >> k[i] >> s[i];

		r[n - 1] = double(d - k[n - 1]) / s[n - 1];
		for (int i = n - 2; i >= 0; --i)
			r[i] = max(double(d - k[i]) / s[i], r[i + 1]);

		double ans = d / r[0];
		cout << fixed << setprecision(7) << ans << endl;
	}	
}