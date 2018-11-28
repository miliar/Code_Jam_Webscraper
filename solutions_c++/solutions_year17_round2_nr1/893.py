#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int T,N,L;
double ans;
//double pos[2000],v[2000];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		ans=0;
		scanf("%d%d",&L,&N);
		for(int i=0;i<N;i++){
			double a,b,c;
			scanf("%lf%lf",&a,&b);
			c=(1.0*L-a)/b;
			ans=max(c,ans);
//			scanf("%llf%llf",&pos[i],&v[i]);
		}
		printf("Case #%d: %.6llf\n",t,L/ans);
	}
	
	return 0;
}
