#include<bits/stdc++.h>
using namespace std;

#define ll long long

ll t,n,k;

int main()
{
	ll i,j,v,f1,f2,a1,a2,c1,c2,x,y,p=0;
	scanf("%lld",&t);
	while(t--)
	{
	    p++;
		scanf("%lld%lld",&n,&k);
		if(n%2)
		{
			v=1;
			f1=n/2;
			c1=2;
			f2=-1;
			c2=0;
		}
		else
		{
			f1=(n-1)/2;
			f2=n/2;
			v=2;
			c1=1;
			c2=1;
		}
		if(k==1)
		{
			if(v==1)
				printf("Case #%lld: %lld %lld\n",p,f1,f1);
			else
				printf("Case #%lld: %lld %lld\n",p,f2,f1);
		}
		else
		{
			k--;
			while(1)
			{
				x=f1,y=f2,a1=c1,a2=c2;
				if(k>c1+c2)
				{
					if(v==1)
					{
						if(x%2)
						{
							f1=x/2,c1=2*a1;
						}
						else
						{
							v=2,f1=(x-1)/2,f2=x/2,c1=a1,c2=a1;
						}
					}
					else
					{
						if(x%2)
						{
							f1=x/2,f2=y/2,c1=2*a1+a2,c2=a2;
						}
						else
						{
							f1=(x-1)/2,f2=x/2,c1=a1,c2=a1+2*a2;
						}
					}
					k=k-a1-a2;
				}
				else
				{
				    if(v==1)
				        printf("Case #%lld: %lld %lld\n",p,x/2,(x-1)/2);
					else if(k<=a2)
						printf("Case #%lld: %lld %lld\n",p,y/2,(y-1)/2);
					else
						printf("Case #%lld: %lld %lld\n",p,x/2,(x-1)/2);
					break;
				}
			}
		}
	}
	return 0;
}
