#include<iostream>
using namespace std;
int main(){
	int T;
	scanf("%d",&T);

	int D,N;
	int K[1004],S[1004];

	for(int t=1;t<=T;++t){

		scanf("%d %d",&D,&N);
		for(int i=0;i<N;++i)
			scanf("%d %d",&K[i],&S[i]);

		double ans = 0;
		for(int i=0;i<N;++i){
			double a;
			a = (D - K[i])/(double)S[i];
			if(i==0){
				ans = D/a;
			}
			else{
				double x = D/a;
				if(ans-x >= 0.000000001)
					ans=x;
			}
		}

		printf("Case #%d: %.7lf\n",t,ans);
	}
	return 0;
}