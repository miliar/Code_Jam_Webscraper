#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
#define EPS 1e-9

int main()
{
	int i,t,n;
	lli d;
	freopen("A-large (1).in","r",stdin);
	freopen("newoutput3.out","w",stdout);
	scanf("%d",&t);
	for(int k=1; k<=t; k++)
	{
		scanf("%lld%d",&d,&n);
		double temp,dist,speed;
		double minm = -1;
		for(i=0;i<n;i++)
		{
		scanf("%lf%lf",&dist,&speed);
		temp=(d-dist)/speed;
		if(temp>minm)
		minm=temp;
		}
		printf("Case #%d: %.6lf\n",k,d/minm);
	}
	return 0;
}
