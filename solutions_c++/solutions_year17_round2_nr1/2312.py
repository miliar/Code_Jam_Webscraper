#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int T;
	double D,N,km,speed;
	scanf("%d",&T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%lf %lf",&D,&N);
		double fastest = 0;
		for (int i = 0; i < N; i++) {
			scanf("%lf %lf",&km, &speed);
			fastest = max(fastest, (D-km)/speed);
		}

		printf("Case #%d: %.6lf\n",tc,D/fastest);
	}
	return 0;
}