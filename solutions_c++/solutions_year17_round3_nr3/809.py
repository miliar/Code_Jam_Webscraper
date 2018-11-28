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

double cal_prob(int N, int K, double* P) {
	double ans = 0;
	return ans;
}
int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int tc, c = 0;
	scanf("%d\n", &tc);

	while (tc--) {
		c++;
		int N, K;
		double U, P[55];
		double s = 0;
		scanf("%d %d %lf", &N, &K,&U);
		F(i, N) scanf("%lf", &P[i]);
		sort(P, P + N);
		P[N] = 1;
		int pivot = 0;
		while (U > 0 && pivot < N) {
			if (U > (P[pivot + 1] - P[pivot]) * (pivot + 1)) {
				U -= (P[pivot + 1] - P[pivot] )* (pivot + 1);
				fill(P, P + pivot+1, P[pivot+1]);
			}
			else{
				fill(P, P + pivot+1, P[pivot] + U / (pivot + 1));
				U = 0;
			}
			pivot++;
		}
		double ans = 1;
		F(i, N) ans *= P[i];
		printf("Case #%d: %lf\n", c, ans);;
	}
	return 0;
}