#include <cstdio>

typedef long double FLOAT;

FLOAT EPS = 1e-8;

int N, D, K[1005], S[1005];
int cases;

FLOAT sabs(FLOAT v) {
	if(v > 0) return v;
	else return -v;
}

bool check(FLOAT t) {
	for(int i = 0; i < N; ++i){
		FLOAT s1 = t * S[i] + K[i];
		if(s1 < D) return false;
	}
	return true;
}

int main() {
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx) {
		scanf("%d%d", &D, &N);
		for(int i = 0; i < N; ++i) {
			scanf("%d%d", &K[i], &S[i]);
		}
		FLOAT l = 0, r = 9999999999999.0;
		for(int i = 0; i < 100; ++i) {
			FLOAT mid = (l + r) / 2;
			if(check(mid)) r = mid;
			else l = mid;
			//printf("l = %.10Lf, r = %.10Lf\n", l, r);
		}
		printf("Case #%d: %.10Lf\n", xx, D * 1.0 / r);
	}
}
