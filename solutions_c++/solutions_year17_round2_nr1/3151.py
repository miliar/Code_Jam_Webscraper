#include <cstdio>
int sp[1024],st[1024];
double solve()
{
	int n,d;
	double maxt=0.0,tt;
	scanf("%d%d",&d,&n);
	for(int xhn=0;xhn<n;xhn++){
		scanf("%d%d",&st[xhn],&sp[xhn]);
	}
	for(int xhn=n-1;xhn>=0;xhn--){
		tt=(double)(d-st[xhn])/sp[xhn];
		if(tt>maxt)
			maxt=tt;
	}
	return (double)d/maxt;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: %.10f\n",i+1,solve());
	}
	return 0;
}
