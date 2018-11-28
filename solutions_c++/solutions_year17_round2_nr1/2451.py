#include <cstdio>

int T,N,D;
double maxv;

int main() {
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++) {
		scanf("%d%d",&D,&N);
		int K,S;
		scanf("%d%d",&K,&S);
		maxv=(double)D/(D-K)*S;
		for(int i=1;i<N;i++) {
			scanf("%d%d",&K,&S);
			double lim=(double)D/(D-K)*S;
			if(maxv>lim) maxv=lim;
		}
		printf("Case #%d: %.12lf\n",cases,maxv);
	}
	return 0;
}
