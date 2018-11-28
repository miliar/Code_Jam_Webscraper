#include<bits/stdc++.h>

using namespace std;

int T,D,N,K,S;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d %d",&D,&N);
		double ans;
		for(int i=0;i<N;i++){
			scanf("%d %d",&K,&S);
			double T = ((double)D-K)/(double)S;
			if (i == 0){
				ans = T;
			}
			ans = max(ans,T);
		}
		printf("Case #%d: %.10lf\n",t,(double)D/ans);
	}
	return 0;
}
