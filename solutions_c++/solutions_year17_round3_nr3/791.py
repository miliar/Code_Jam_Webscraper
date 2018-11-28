#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long ll;

const int MAX_N = 50;
int n;
int k;
double u;
double p[MAX_N + 1];

double solve() {
	scanf("%d%d%lf", &n, &k, &u);
	for (int i=0; i<n; i++) {
		scanf("%lf", &p[i]);
	}
	sort(p, p+n);
	p[n] = 1;

	int i;
	double product;
	for (i=0; i<n; i++) {
		double need = (p[i+1] - p[i]) * (i+1);
		if (u > need && i!=n-1) {
			u -= need;
		} else {
			product = pow(p[i] + u/(i+1), (i+1));
			break;
		}
	}
	for (i++; i<n; i++) {
		product *= p[i];
	}
	return product;
}

int main() {
	int t;
	scanf("%d\n", &t);

	for (int i=1; i<=t; i++) {
		printf("Case #%d: %.9f\n", i, solve());
	}
}
