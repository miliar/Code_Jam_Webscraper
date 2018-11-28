#include<bits/stdc++.h>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,_,n,m,i,a,b;
	double s;
	for(scanf("%d",&T),_=1;_<=T;_++)
	{
		scanf("%d%d",&m,&n);
		for(s=i=0;i<n;i++) {
			scanf("%d%d",&a,&b);
			s=max(s,1.0*(m-a)/b);
		}
		printf("Case #%d: %.10f\n",_,m/s),fprintf(stderr,"Case #%d: %.10f\n",_,m/s);
	}
	return 0;
}
