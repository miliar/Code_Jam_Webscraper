#include<iostream>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int N,K;
		scanf("%d %d",&N,&K);
		double u,p[52];
		int P[52],U;
		scanf("%lf",&u);
		U = u*1000000;
		for(int i=0;i<N;++i){
			scanf("%lf",&p[i]);
			P[i]=p[i]*1000000;
		}

		for(int i=0;i<U;++i){
			int idx=0,kam=P[0];;
			for(int j=1;j<N;++j){
				if(kam > P[j]){
					idx = j;
					kam=P[j];
				}
			}
			P[idx]++;
		}
		double ans=1;
		for(int i=0;i<N;++i){
			ans=ans*(double)P[i]/1000000.0;
		}
		printf("Case #%d: %.9lf\n",t,ans);
	}
}