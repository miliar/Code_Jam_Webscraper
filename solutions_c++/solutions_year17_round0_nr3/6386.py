#include <map>
#include <cstdlib>
#include <cstdio>
#include <cfloat>
#include <vector>
#include <cmath>
using namespace std;

void recurse (int n, int k, int *L, int *R) {
    if (k == 1) {
        n--;
        *L = n/2;
        *R = n - n/2;
    } else if (k == 0) {
        *L = 10000000;
        *R = 10000000;
    } else {
        int M1, M2, m1, m2;
        n--;
        k--;
        recurse(n/2, k/2, &M1, &m1);
        recurse(n - n/2, k - k/2, &M2, &m2);
        *L = min(M1,M2);
        *R = min(m1,m2);
    }
}

double solve () {
    int N,K;
    scanf("%d %d", &N, &K);
    int L, R;
    recurse (N, K, &L, &R);   
    printf("%d %d\n", max(L,R), min(L,R));
}

int main () {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
        solve();
    }

	return 0;
}
