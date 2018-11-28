#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <assert.h>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

#define mp make_pair
#define loop(i,n) for(int i=0; i<n; i++)
#define pii pair<int,int>
#define ll long long
#define ld long double

const int MXN = 1005;
const ld EPS = 0.000000001;

long long D, N;
long long K[MXN], S[MXN];

int main () {
	int tests;
	scanf("%d", &tests);
	for (int test=1; test<=tests; test++) {
		scanf("%lld%lld", &D, &N);
		for (int i=0; i<N; i++) scanf("%lld%lld", &K[i], &S[i]);
		ld slowest = 0;
		for (int i=0; i<N; i++) slowest = max(slowest, (ld) (D - K[i]) * 1.0 / S[i]);
		printf("Case #%d: %.10Lf\n", test, D / slowest);
	}
	return 0;
}