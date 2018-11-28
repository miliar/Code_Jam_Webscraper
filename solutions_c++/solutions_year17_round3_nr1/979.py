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
#define M_PI 3.14159265358979323846

bool myfunc(Pll a, Pll b) {
	return (a.first > b.first);
}

bool myfunc2(Pll a, Pll b) {
	return (a.second > b.second);
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int tc, c = 0;
	scanf("%d\n", &tc);

	while (tc--) {
		c++;
		int N, K;
		ll R[1010], H[1010];
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N;i++) scanf("%lld %lld", &R[i], &H[i]);
		
		ll ans = 0;

		vector<Pll> aa;
		F(i, N) aa.pb(make_pair(R[i] *R[i], 2 * R[i] * H[i]));
		sort(all(aa), myfunc);
		
		F(i, N) {
			if (i + K <= N) {
				ll tmp = aa[i].first;
				vector<Pll> bb = aa;
				sort(bb.begin() + i+1, bb.end(), myfunc2);
				F(j, K) tmp += bb[i + j].second;
				if (ans < tmp) ans = tmp;
			}
		}
		double d_ans = ans * M_PI;
		printf("Case #%d: %f\n", c, d_ans);;
	}
	return 0;
}