#include <map>
#include <cstdlib>
#include <cstdio>
#include <cfloat>
#include <vector>
#include <cmath>
using namespace std;

double solve () {
    int N, D;

    scanf("%d %d", &D, &N);

    double tmax = 0.;
    for (int i = 0; i < N; i++) {
        int k, s;
        scanf("%d %d", &k, &s);
        double t = (D - k) / (s + 0.);
        tmax = max(tmax, t);
    }
    return D / tmax;
}

int main () {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: %f\n", i, solve());
    }

	return 0;
}
