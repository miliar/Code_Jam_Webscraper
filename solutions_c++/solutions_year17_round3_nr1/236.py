#define _CRT_SECURE_NO_WARNINGS
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

#define MEMSET(x, WITH) memset(x, (WITH), sizeof(x))
#define FOR(i, E) for (int i=0; i<(E); i++)
typedef long long ll;
//const ll MOD = 1000000007;
const double PI = atan(1) * 4;



pair<double, double> arr[1003];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		printf("Case #%d: ", tc);

		int N, K; scanf("%d%d", &N, &K);
		FOR(i, N) {
			int R, H; scanf("%d%d", &R, &H);

			arr[i].first = 2 * PI * R * H;
			arr[i].second = PI * R * R;
		}

		sort(arr, arr + N);
		reverse(arr, arr + N);

		double S = 0;
		FOR(i, K-1) S += arr[i].first;
		double SS = S + arr[K-1].first;
		

		double ans = -123;
		FOR(i, K) ans = max(ans, SS + arr[i].second);

		for (int i=K; i<N; i++) ans = max(ans, S + arr[i].first + arr[i].second);


		printf("%.10lf\n", ans);

	}

	return 0;
}
