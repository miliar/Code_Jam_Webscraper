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
		int N, Q, E[110], S[110], U[110], V[110];
		int D[110][110];
		double ans;
		scanf("%d %d", &N, &Q);
		F(i, N) scanf("%d %d", &E[i+1], &S[i+1]);
		F(i, N) F(j,N) scanf("%d ", &D[i+1][j+1]);
		F(i, Q) scanf("%d %d", &U[i+1], &V[i+1]);

		double time[110];
		fill(time, time + 110, 1.79769e+308);
		time[1] = 0;
		for (int i = 1; i <= N; i++) {
			int j = i + 1;
			int dist = D[i][j];
			while(dist <= E[i]){
				if (time[j] > time[i] + 1.0*dist / S[i]) time[j] = time[i] + 1.0*dist / S[i];
				if (j == N) break;
				dist += D[j][j + 1];
				j++;
			}
		}
		
		printf("Case #%d: %f\n", c, time[N]);
	}
	return 0;
}