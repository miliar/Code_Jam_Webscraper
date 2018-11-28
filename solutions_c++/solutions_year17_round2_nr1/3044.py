#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <deque>
#include <queue>
#include <functional>
#include <string>


using namespace std;

long int D, N;
long int K[1001], S[1001];

int main(int argc, char** argv) {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	setbuf(stdout, NULL);

	int T;
	int test_case;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {

		float ans;
		long double mintime=0;
		scanf("%ld %ld", &D, &N);
		for (int i = 0; i < N; ++i) {
			scanf("%ld %ld", &K[i], &S[i]);
			if (mintime < (float)(D - K[i]) / S[i]) {
				mintime = (float)(D - K[i]) / S[i];
			}
		}
		ans = D / mintime;
		

		printf("Case #%d: ", test_case);
		printf("%.6lf\n", ans);
	}

	return 0;	
}

