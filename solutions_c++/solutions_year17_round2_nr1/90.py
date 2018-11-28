#include <stdio.h>

int main(){
	int jcase;
	double D;
	int N;
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%lf %d", &D, &N);
		double lastTime = 0;
		
		for(int i=0; i<N; i++){
			double pos, speed;
			scanf("%lf %lf", &pos, &speed);
			pos = D - pos;
			double time = pos / speed;
			if(time > lastTime) lastTime = time;
		}
		
		double ans = D / lastTime;
		printf("Case #%d: %.7lf\n", icase+1, ans);
	}
	return 0;
}
