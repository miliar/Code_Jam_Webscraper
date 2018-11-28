#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxN 100
#define maxP 4

int g[maxN], dp[maxN][maxN][maxN][maxN][maxP], N, P;

int solve(int a, int b, int c, int d, int e) {
	if (a < 0 || b < 0 || c < 0 || d < 0) return -INF;
	if (!a && !b && !c && !d) return 0;
	if (~dp[a][b][c][d][e]) return dp[a][b][c][d][e];
	return dp[a][b][c][d][e] = !e + max(solve(a-1, b, c, d, (e+0)%P),
		max(solve(a, b-1, c, d, (e + 1) % P),
			max(solve(a, b, c-1, d, (e + 2) % P), solve(a, b, c, d-1, (e + 3) % P))));
}

int main() {
	int T, caso=1;
	cin >> T;
	while (T--) {
		cin >> N >> P;
		int a=0, b=0, c=0, d=0;
		FOR(i, 0, N) {
			cin >> g[i];
			switch (g[i] % P) {
			case 0:
				a++;
				break;
			case 1:
				b++;
				break;
			case 2:
				c++;
				break;
			case 3:
				d++;
				break;
			}
		}
		memset(dp, -1, sizeof(dp));
		int ans = solve(a, b, c, d, 0);
		cerr << "Case #" << caso << ": " << ans << endl;
		cout << "Case #" << caso++ << ": " << ans;
		cout << endl;
	}
	return 0;
}
