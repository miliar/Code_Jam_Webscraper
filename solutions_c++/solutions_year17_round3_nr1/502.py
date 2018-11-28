#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cctype>
#include <cstring>
#include <bitset>
#include <algorithm>
#include <iomanip>

#define ld long double
#define ll long long
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define y0 _y0
#define y1 _y1

using namespace std;

template < typename T > T abs(T x)
{
    return x > 0 ? x : -x;
}

template < typename T > T sqr(T x)
{
    return x * x;
}

ll dp[2005][2005];
ld pi = 3.14159265359;

int main()
{
	freopen("input11.txt", "r", stdin);
	freopen("output11.txt", "w", stdout);
	
	int t;
	cin >> t;
	int initt = t;
	
	while (t--) {
		int n, k;
		
		cin >> n >> k;
		
		vector < pair <ll, ll> > a;
		
		for (int i = 0; i < n; i++) {
			int x, y;
			cin >> x >> y;
			a.pb(mp(x, y));
		}
		
		sort(a.begin(), a.end());
		reverse(a.begin(), a.end());
		
		for (int i = 0; i <= n + 1; i++)
			for (int j = 0; j <= n + 1; j++)
				dp[i][j] = -1;
		
		dp[0][0] = 0;
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				if (dp[i][j] == -1) continue;
				ll r = a[i].fst;
				ll h = a[i].snd;
				dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 2 * r * h + (j == 0 ? sqr(r) : 0));
				dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
			}
		}
		
		ld ans = dp[n][k] * pi;
		
		cout << "Case #" << initt - t << ": ";
		
		cout << fixed << setprecision(10) << ans;
		
		cout << "\n"; 
	}	
    return 0;   
}


