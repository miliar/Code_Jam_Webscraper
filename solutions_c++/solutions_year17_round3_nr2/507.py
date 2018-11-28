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

bool bizy1[2005], bizy2[2005];
int dp[2005][2005][2];

int main()
{
	freopen("input22.txt", "r", stdin);
	freopen("output22.txt", "w", stdout);
	
	int t;
	cin >> t;
	int initt = t;
	
	while (t--) {
		int n, m;
		
		int H = 60 * 24;
		
		for (int i = 0; i <= H; i++) {
			bizy1[i] = false;
			bizy2[i] = false;
		}
		
		cin >> n >> m;
		
		if (n + m == 0) {
			cout << "Case #" << initt - t << ": 2\n";
			continue;
		}
		
		for (int i = 0; i < n; i++) {
			int x, y;
			
			cin >> x >> y;
			for (int j = x; j < y; j++)
				bizy1[j] = 1;
		}
		
		for (int i = 0; i < m; i++) {
			int x, y;
			
			cin >> x >> y;
			for (int j = x; j < y; j++)
				bizy2[j] = 1;
		}
		
		int pos = 0;
		
		for (int i = 0; i < H; i++) {
			if (bizy1[i] || bizy2[i]) {
				pos = i;
				break;
			}
		}
			
		for (int i = pos; i < H; i++) {
			bizy1[i - pos] = bizy1[i];
			bizy2[i - pos] = bizy2[i];
		}
		
		for (int i = H - pos; i < H; i++) {
			bizy1[i] = false;
			bizy2[i] = false;
		}
				
		int inf = 10000000;
			
		for (int i = 0; i <= H + 5; i++)
			for (int j = 0; j <= H + 5; j++)
				for (int k = 0; k < 2; k++)
					dp[i][j][k] = inf;
				
		if (!bizy1[0]) {
			dp[0][1][0] = 0;
		}
		if (!bizy2[0]) {
			dp[0][0][1] = 0;
		}
		
		for (int i = 0; i < H; i++) {
			for (int j = 0; j <= min(i + 1, H / 2 + 1); j++) {
				if (dp[i][j][0] < inf) {
					if (!bizy1[i + 1])
						dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][0] + (i + 1 == H-1 ? bizy1[0] : 0));
					if (!bizy2[i + 1]) 
						dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][0] + 1 + (i + 1 == H-1 ? bizy2[0] : 0));
				}
				if (dp[i][j][1] < inf) {
					if (!bizy1[i + 1])
						dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][1] + 1 + (i + 1 == H-1 ? bizy1[0] : 0));
					if (!bizy2[i + 1]) 
						dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][1] + (i + 1 == H-1 ? bizy2[0] : 0));
				}
			}
		}
		
		int ans = min(dp[H - 1][H / 2][0], dp[H - 1][H / 2][1]);
		
		cout << "Case #" << initt - t << ": ";
		
		cout << ans;
		
		cout << "\n"; 
	}	
    return 0;   
}


