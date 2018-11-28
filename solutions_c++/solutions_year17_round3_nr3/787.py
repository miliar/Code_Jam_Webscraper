#include<bits/stdc++.h>
using namespace std;
double P[50],U;
int main(){
	freopen("C-small-1-attempt1.in","r",stdin);
	freopen("C-small-1-attempt1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int ST=0;ST<T;ST++){
		int n,k;
		scanf("%d%d%lf",&n,&k,&U);
		for(int j=0;j<n;j++)scanf("%lf",&P[j]);
		sort(P,P+n);
		int F;
		for(F=0;F<n;F++){
			double t=0;
			for(int i=0;i<F;i++){
				t+=P[F]-P[i];
			}
			if(t>U)break;
		}
		for(int i=0;i<F;i++){
			U-=P[F-1]-P[i];
			P[i]=P[F-1];
		}
		for(int i=0;i<F;i++){
			P[i]+=U/F;
		}
		double ans=1;
		for(int i=0;i<n;i++)ans=ans*P[i];
		printf("Case #%d: %f\n",ST+1,ans);
	}
}
