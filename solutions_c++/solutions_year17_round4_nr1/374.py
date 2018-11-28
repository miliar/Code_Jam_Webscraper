#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cassert>
#include <bitset>
#include <fstream>
#include <stack>
#include <cstdlib>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define fst first
#define snd second
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double

template < typename T>
T sqr(T x) {
	return x * x;
}

template < typename T>
T abs(T x) {
	return x > 0 ? x : -x;
}

//////////////////////////////////////////////////

const int maxn = 103;
int dp[maxn][maxn][maxn][4];
const int INF = 1e9;

void solve() {
	int n, p;
	cin >> n >> p;
	vector < int > a(p);
	for (int i = 1; i <= n; i++) {
		int x;
		cin >> x;
		a[x%p]++;
	}
	if (p == 2) {
		cout << n - a[1] / 2 << "\n";
		return;
	}
	if (p == 3) {
		int mini = min(a[1], a[2]), maxi = max(a[1], a[2]);
		int delta = maxi - mini;
		cout << a[0] + mini + (delta + 2) / 3 << "\n";
		return;
	}
	cout << a[0] + dp[a[1]][a[2]][a[3]][0] << "\n";
}

int main() {
	//srand(time(NULL));
	#ifdef LOCAL	
		//gen();
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
		//cout << endl << endl;
	#else
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
	#endif
	//check();
	
	//ios_base::sync_with_stdio(false);
	
	for (int i = 0; i < maxn; i++) {
		for (int j = 0; j < maxn; j++) {
			for (int k = 0; k < maxn; k++) {
				for (int bal = 0; bal < 4; bal++) {					
					if (i == 0 && j == 0 && k == 0) {
						if (bal == 0) {
							continue;
						} else {
							dp[i][j][k][bal] = 0;
							continue;
						}
					}
					int c = 0;
					if (bal == 0) {
						c++;
					}
					dp[i][j][k][bal] = -INF;
					if (i > 0) {
						dp[i][j][k][bal] = max(dp[i][j][k][bal], dp[i-1][j][k][(bal+1)%4] + c);
					}
					if (j > 0) {
						dp[i][j][k][bal] = max(dp[i][j][k][bal], dp[i][j-1][k][(bal+2)%4] + c);
					}
					if (k > 0) {
						dp[i][j][k][bal] = max(dp[i][j][k][bal], dp[i][j][k-1][(bal+3)%4] + c);
					}
				}
			}
		}
	}
	
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": ";
		solve();
	}
	
	return 0;
}
