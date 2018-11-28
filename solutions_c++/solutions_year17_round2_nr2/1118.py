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
bool myfunc(pair<char, int> a, pair<char, int> b) {
	return (a.second > b.second);
}
int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int tc, c = 0;
	scanf("%d\n", &tc);

	while (tc--) {
		c++;
		int N, R, O, Y, G, B, V;
		vector<char> ans;
		scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
		vector<pair<char, int>> Uni;
		Uni.pb(make_pair('R', R));
		Uni.pb(make_pair('O', O));
		Uni.pb(make_pair('Y', Y));
		Uni.pb(make_pair('G', G));
		Uni.pb(make_pair('B', B));
		Uni.pb(make_pair('V', V));
		sort(all(Uni), myfunc);

		char sc[10];
		int sn[10];
		F(i, 6) {
			sc[i] = Uni[i].first;
			sn[i] = Uni[i].second;
		}
		if (sn[0] > sn[1] + sn[2]) printf("Case #%d: IMPOSSIBLE\n", c);
		else {
			F(i, sn[1] - sn[2]) {
				ans.pb(sc[1]);
				ans.pb(sc[0]);
				sn[0]--;
			}
			F(i, sn[2]) {
				ans.pb(sc[1]);
				if (sn[0]) {
					ans.pb(sc[0]);
					sn[0]--;
				}
				ans.pb(sc[2]);
				if (sn[0]) {
					ans.pb(sc[0]);
					sn[0]--;
				}
			}
			printf("Case #%d: ", c);
			for (auto i : ans) printf("%c", i);
			printf("\n");
		}
	}
	return 0;
}