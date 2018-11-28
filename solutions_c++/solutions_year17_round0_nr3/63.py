#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<list>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<functional>
#include<cmath>
#include<string>

#define sd(a) scanf("%d", &a);
#define sld(a) scanf("%lld", &a);

using namespace std;

typedef long long int lli;
typedef pair<lli, lli> ii;

int xx[4] = { 0, 0, -1, 1 };
int yy[4] = { -1, 1, 0, 0 };

ii recursion(lli N1, lli cou1, lli N2, lli cou2, lli K) {
	if (K <= cou1) {
		return ii(N1 / 2, (N1 - 1) / 2);
	}
	else if (K <= cou1 + cou2) {
		return ii(N2 / 2, (N2 - 1) / 2);
	}

	lli next1 = cou1;
	lli next2 = cou2;
	if (N1 % 2 == 1) {
		next1 += cou1;
		next1 += cou2;
	}
	else {
		next2 += cou1;
		next2 += cou2;
	}

	return recursion(N1 / 2, next1, (N2 - 1) / 2, next2, K - cou1 - cou2);
}

int main(void) {
	int TEST;
	scanf("%d", &TEST);
	for (int CASE = 1; CASE <= TEST; CASE++) {
		lli N, K;
		sld(N); sld(K);

		ii ans = recursion(N, 1, N - 1, 0, K);

		printf("Case #%d: %lld %lld\n", CASE, ans.first, ans.second);
	}

	return 0;
}