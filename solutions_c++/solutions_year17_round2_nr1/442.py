#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output_A-large.txt","w",stdout);
	int t,d,n,i,ct,k,s,num=1;
	double l,r,mid,tt,mc,res;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&d,&n);
		mc=0;
		for(i=0;i<n;i++) 
		{
			scanf("%d%d",&k,&s);
			tt=(double)(d-k)/s;
			mc=max(mc,tt);
		}
		l=0;
		r=10000000000005;
		ct=0;
		while(ct<=100000)
		{
			ct++;
			mid=(l+r)/2;
			if(mc<=d/mid)
			{
				res=mid;
				l=mid;
			}
			else r=mid;
		}
		printf("Case #%d: %.6f\n",num++,res);
	}
}