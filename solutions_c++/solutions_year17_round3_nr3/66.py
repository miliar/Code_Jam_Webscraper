#include <bits/stdc++.h>
#define eps 1e-12
double add, p[111];
int n, m;
void Main(){
	scanf("%d%d%lf", &n, &m, &add);
	for (int i = 0; i < n; i ++ )
		scanf("%lf", &p[i]);
	std::sort(p, p + n);
	for (; add > eps; ){
		int same = 0;
		for (; p[same + 1] - p[same] < eps && same < n - 1; same ++ );
		double del = p[same + 1] - p[same];
		if (del > 0 && del * same + del <= add){
			for (int i = 0; i <= same; i ++ ){
				p[i] += del;
				add -= del;
			}
		}
		else{
			double piece = add / (same + 1);
			for (int i = 0; i <= same; i ++ ){
				p[i] += piece;
				add -= piece;
			}
		}
		//for (int i = 0; i < n; i ++ )
		//	printf("%f ", p[i]);
		//printf("|%f\n", add);
	}
	double res = 1;
	for (int i = 0; i < n; i ++ )
		res *= p[i];
	printf("%.10lf\n", res);
}
int main(){
	freopen("t.out","w",stdout);
	int _;
	scanf("%d", &_);
	for (int i = 1; i <= _; i ++ ){
		printf("Case #%d: ", i);
		Main();
	}
}
