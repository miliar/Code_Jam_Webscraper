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

bool myfunc(Pi a, Pi b) {
	return (a.first < b.first);
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int tc, c = 0;
	scanf("%d\n", &tc);

	while (tc--) {
		c++;
		int Ac, Aj;
		vector<Pi> wc, wj;
		scanf("%d %d", &Ac, &Aj);
		F(i, Ac) {
			int t1, t2;
			scanf("%d %d", &t1, &t2);
			wc.pb(make_pair(t1, t2));
		}
		F(i, Aj) {
			int t1, t2;
			scanf("%d %d", &t1, &t2);
			wj.pb(make_pair(t1, t2));
		}
		sort(all(wc), myfunc);
		sort(all(wj), myfunc);

		int ans = 0;
		if (Ac == 2) {
			if (wc[1].second - wc[0].first <= 720 || 1440 + wc[0].second - wc[1].first <= 720) ans = 2;
			else ans = 4;
		}
		else if(Aj == 2) {
			if (wj[1].second - wj[0].first <= 720 || 1440 + wj[0].second - wj[1].first <= 720) ans = 2;
			else ans = 4;
		}
		else ans = 2;
		printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}