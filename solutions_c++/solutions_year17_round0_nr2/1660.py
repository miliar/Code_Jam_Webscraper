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

int dp[25][15][3];
int from[25][15][3];

int main()
{
	freopen("input2.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	
	int t;
	
	cin >> t;
	
	int initt = t;
	
	while (t--) {
		ll n;
		cin >> n;
		
		vector <int> a;
		
		for (int i = 0; i < 20; i++) {
			a.pb(n % 10);
			n /= 10;
		}
		
		for (int i = 0; i < 25; i++)
			for (int j = 0; j < 15; j++)
				for (int k = 0; k < 3; k++) {
					dp[i][j][k] = -1;
				}
		
		for (int i = 0; i < 10; i++) {
//			int ind = 0;
//			if (i == a[0]) ind = 1;
//			if (i > a[0]) ind = 2;
			if (dp[0][i][i > a[0]] < i) {
				dp[0][i][i > a[0]] = 0;
			}
		}
		
		for (int i = 0; i < 19; i++) {
			for (int h = 0; h < 10; h++)
				for (int j = 0; j < 2; j++) {
					if (dp[i][h][j] == -1) continue;
					for (int k = 0; k <= h; k++) {
						int ind = 0;
						if (k == a[i + 1]) ind = j;
						if (k > a[i + 1]) ind = 1;
						if (dp[i + 1][k][ind] < h) {
							dp[i + 1][k][ind] = h;
							from[i + 1][k][ind] = j;
						}
					}	
				}
		}
		
		vector <int> ans;
		bool f = 0;
		int j = 0;
		int h = 0;
		
		for (int i = 19; i >= 0; i--) {
			int v = h;
			if (v == 0 && !f) {
				
			}
			else {
				ans.pb(v);
				f = 1;
			}
			int jt = j;
			j = from[i][h][jt];
			h = dp[i][h][jt];
		}
		
		cout << "Case #" << initt - t << ": ";
		for (int i = 0; i < ans.size(); i++)
			cout << ans[i];
		cout << "\n"; 
	}	
    return 0;   
}

