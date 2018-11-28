#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <list>
#include <set>
#include <map>

#define MIN(a, b) (a < b ? a : b)
#define MAX(a, b) (a > b ? a : b)

using namespace std;

typedef struct data {
	int k;
	int s;
} data_t;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);'

	int T;
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		int D, N;
		scanf("%d %d", &D, &N);

		vector<data_t> datum(N);
		for (int n = 0; n < N; n++) {
			data_t data;
			scanf("%d %d", &data.k, &data.s);
			
			datum[n] = data;
		}

		double max = (double)(D - datum[0].k) / datum[0].s;
		for (int n = 0; n < N; n++) {
			max = MAX(max, (double)(D - datum[n].k) / datum[n].s);
		}

		printf("Case #%d: %f\n", t + 1, D / max);
	}

	return 0;
}