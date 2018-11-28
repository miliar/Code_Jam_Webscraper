#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
#include <vector>
#include <stack>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> Pi;
typedef pair<ll, ll> Pll;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define F(i, n) for(int i=0;i<n;i++)
#define F1(i, n) for(int i=1;i<=n;i++)
#define all(x) x.begin(), x.end()

#define ABS(x) (((x) > 0 ) ? (x) : (-(x)))
#define MAX2(x, y) (((x) > (y)) ? (x) : (y))
#define MIN2(x, y) (((x) < (y)) ? (x) : (y))
#define MAX3(x, y, z) ( (x) > (y)  ? ( (x) > (z) ? (x) : (z)  ) : ( (y) > (z) ? (y) : (z) )  )
#define MIN3(x, y, z) ( (x) < (y)  ? ( (x) < (z) ? (x) : (z)  ) : ( (y) < (z) ? (y) : (z) )  )
#define MID3(val1,val2,val3) MAX2(MIN2(MAX2(val1,val2),val3),MIN2(val1,val2))

#define INF 2147483647
#define IINF 9123456789123456789

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int tc, c = 0;
	scanf("%d\n", &tc);

	while (tc--) {
		c++;
		int D, N;
		int K[1010], S[1010];
		double ans, time[1010];
		scanf("%d %d\n", &D, &N);
		F(i, N) scanf("%d %d", &K[i], &S[i]);
		F(i, N) {
			time[i] = 1.0*(D - K[i]) / S[i];
		}
		double _max = *max_element(time, time + N);
		ans = D / _max;
		F(i, N) {
			for (int j = i + 1; j < N; j++) {
				double tmp = (S[j] * K[i] + S[j] * K[j]) / (K[i] - K[j]);
				if (ans < tmp) ans = tmp;
			}
		}
		ans = D / _max;
		printf("Case #%d: %f\n", c, ans);
	}
	return 0;
}