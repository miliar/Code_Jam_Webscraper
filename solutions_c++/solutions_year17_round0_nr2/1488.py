#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long i64;

int T;
i64 N;

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T; ) {
		scanf("%lld", &N);
		N = N * 9 + 9;
		vector<i64> cand;
		for (int i = 0; i < 9; ++i) cand.push_back(0LL);
		i64 v = 1;
		while (N) {
			for (int i = 0; i < (int)(N % 10); ++i) {
				cand.push_back(v - 1);
			}
			v *= 10;
			N /= 10;
		}
		i64 ret = 0;
		for (int i = 0; i < 9; ++i) {
			ret += cand.back();
			cand.pop_back();
		}
		printf("Case #%d: %lld\n", t, ret / 9);

	}
	return 0;
}
