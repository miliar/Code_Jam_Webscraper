#include <bits/stdc++.h>
#define maxn 1020
using namespace std;
int n,m;
double p[maxn];
double u;


int main()
{
	freopen("B-small1.in","r",stdin);
	freopen("B-small1.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%d%d",&n,&m);
		scanf("%lf",&u);
		for (int i=1;i<=n;i++) scanf("%lf",&p[i]);
		sort(p+1, p+n+1);

		double avg=u;
		for (int i=1;i<=n;i++)
			avg+=p[i];
		avg/=n;
		if (avg>1) avg=1;

		double ans=1;
		int st=n;
		p[n+1]=1.0;
		for (int i=1;i<=n;i++)
			if (u>=(p[i+1]-p[i])*i){
				u-=(p[i+1]-p[i])*i;
				p[i]=p[i+1];
			}
			else{
				p[i]+=u/i;
				st=i;
				break;
			}
		// cout<<st<<endl;
		// for (int i=1;i<=n;i++) cout<<p[i]<<' '; cout<<endl;
		for (int i=1;i<=st;i++)
			ans*=p[st];
		for (int i=st+1;i<=n;i++)
			ans*=p[i];
		printf("Case #%d: %.6f\n",o,  ans);
	}

	return 0;
}