#include <cstdio>
#include <algorithm>

using namespace std;

double D, v, x;
int T;

int main() {
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d", &T);
	for (int ii=1;ii<=T;++ii) {
		int N;
		printf("Case #%d: ", ii);
		scanf("%lf %d", &D, &N);
		double v_res = -1.0;
		for (int i=0;i<N;++i) {
			double vv;
			scanf("%lf %lf",&x, &v);
			vv = v * D / (D - x);
			if (i == 0 ||  vv < v_res) {
				v_res = vv;
			}
		}
		printf("%.6lf\n", v_res);
	}

	return 0;
}