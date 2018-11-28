#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define MOD
#define ADD(X,Y) ((X) = ((X) + (Y)%MOD) % MOD)
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;

int T;
int N, P;
i64 R[100], Q[100][100];

i64 rup(i64 a, i64 b)
{
	return a / b + (a % b ? 1 : 0);
}
pair<i64, i64> range(i64 target, i64 has)
{
	return{ rup(has, target / 10 * 11), has / (target / 10 * 9) };
}

pair<i64, i64> W[100][100];
int ki[100], prep[100];

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;) {
		scanf("%d%d", &N, &P);
		for (int i = 0; i < N; ++i) {
			scanf("%lld", R + i);
			R[i] *= 10;
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < P; ++j) {
				scanf("%lld", &(Q[i][j]));
				Q[i][j] *= 10;

				W[i][j] = range(R[i], Q[i][j]);
			}
		}
		vector<pair<int, int> > eve;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < P; ++j) {
				if (W[i][j].first <= W[i][j].second) {
					eve.push_back({ W[i][j].first, ~i });
					eve.push_back({ W[i][j].second, i });
				}
			}
		}
		for (int i = 0; i < N; ++i) ki[i] = prep[i] = 0;

		int ret = 0;
		sort(eve.begin(), eve.end());
		for (auto a : eve) {
			if (a.second < 0) {
				int v = ~a.second;
				++ki[v];
				bool flg = true;
				for (int i = 0; i < N; ++i) {
					if (ki[i] == 0) flg = false;
				}
				if (flg) {
					++ret;
					for (int i = 0; i < N; ++i) {
						--ki[i];
						++prep[i];
					}
				}
			} else {
				int v = a.second;
				if (prep[v] > 0) --prep[v];
				else --ki[v];
			}
		}
		for (int i = 0; i < N; ++i) {
			if (prep[i] != 0 || ki[i] != 0) fprintf(stderr, "waf\n");
		}
		printf("Case #%d: %d\n", t, ret);
	}

	return 0;
}
