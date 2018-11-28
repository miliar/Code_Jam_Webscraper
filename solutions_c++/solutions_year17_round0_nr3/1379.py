#include"stdio.h"
#include"algorithm"
#include"map"
using namespace std;
typedef long long LL;
int T;
LL N, K, ANS;
map<LL, LL> M;
map<LL, LL>::iterator it;
int main() {
	//freopen("C-small-1-attempt0.in", "r", stdin);
	//freopen("C-small-1-attempt0.txt", "w", stdout);
	//freopen("C-small-2-attempt0.in", "r", stdin);
	//freopen("C-small-2-attempt0.txt", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%lld%lld", &N, &K);
		M.clear();
		M[-N] = 1;
		while (K > 0) {
			it = M.begin();
			LL P = -(it -> first) - 1, Q = it -> second;
			ANS = P;
			K -= Q;
			M[-(P / 2)] += Q;
			M[-(P / 2 + P % 2)] += Q;
			M.erase(it);
		}
		printf("Case #%d: %lld %lld\n", t, ANS / 2 + ANS % 2, ANS / 2);
	}
}
