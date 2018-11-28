#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <iomanip>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

typedef long double ld;

int T;
int D, N;

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d", &D, &N);
		ld res = 1e30l;
		for (int i = 0; i < N; i++) {
			int k, s; scanf("%d %d", &k, &s);
			res = min(res, ld(D) * s / ld(D - k));
		}
		printf("Case #%d: ", tc);
		cout << fixed << setprecision(10) << res << endl;
	}
	return 0;
}