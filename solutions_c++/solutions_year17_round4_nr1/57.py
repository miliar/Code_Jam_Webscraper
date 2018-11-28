#define _USE_MATH_DEFINES
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <cfloat>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <vector>
#include <random>
#include <unordered_map>
using namespace std;

#define rep(i, N) for (int i = 0; i < N; i++)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> i_i;
typedef pair<ll, int> ll_i;
typedef pair<double, int> d_i;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> d_d;
struct edge { int u, v; ll w; };

int const MOD = 1000000007;
ll _MOD = 1000000009;
double EPS = 1e-12;
int INF = INT_MAX / 10;

short dp[102][102][102][102];

void f(short& x, short y) { x = max(x, y); }

int main() {
	int T; cin >> T;
	rep(t, T) {
		int N, M; cin >> N >> M;
		vector<int> num(4);
		rep(i, N) {
			int x; cin >> x;
			num[x % M]++;
		}
		rep(i0, num[0] + 1)
			rep(i1, num[1] + 1)
				rep(i2, num[2] + 1)
					rep(i3, num[3] + 1)
						dp[i0][i1][i2][i3] = -10000;
		dp[0][0][0][0] = 0;
		rep(i0, num[0] + 1)
			rep(i1, num[1] + 1)
				rep(i2, num[2] + 1)
					rep(i3, num[3] + 1) {
						int x = (i0*0 + i1*1 + i2*2 + i3*3) % M;
						if (i0 + 1 <= num[0])
							f(dp[i0 + 1][i1][i2][i3], dp[i0][i1][i2][i3] + !x);
						if (i1 + 1 <= num[1])
							f(dp[i0][i1 + 1][i2][i3], dp[i0][i1][i2][i3] + !x);
						if (i2 + 1 <= num[2])
							f(dp[i0][i1][i2 + 1][i3], dp[i0][i1][i2][i3] + !x);
						if (i3 + 1 <= num[3])
							f(dp[i0][i1][i2][i3 + 1], dp[i0][i1][i2][i3] + !x);
					}
		int ans = dp[num[0]][num[1]][num[2]][num[3]];
		printf("Case #%d: %d\n", t + 1, ans);
	}
}
