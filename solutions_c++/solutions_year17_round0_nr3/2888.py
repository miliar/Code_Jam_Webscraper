#include<bits/stdc++.h>

#define ll long long

int main()
{
	ll t,j;
	scanf("%lld",&t);
	for(j=0;j<t;j++)
	{
		printf("Case #%lld: ",j+1);
		ll n,k;
		scanf("%lld%lld",&n,&k);
		ll a[100000][2]={0},f[100000][2]={0},temp,t1,t2,c=4,i,max1,min1,max2,min2,ans=0,flag=0;
		temp=n;
		a[0][0]=temp;
		f[0][0]=1;
		i=1;
		if(n==1)
		{
			printf("0 0\n");
			continue;
		}
		if(k==1)
		{
			temp--;
			printf("%lld %lld\n",temp-temp/2,temp/2);
			continue;
		}
		ans+=f[0][0];
		while(a[i-1][0]!=1&&ans<k)
		{	
			temp=a[i-1][0]-1;
			max1=temp-temp/2;
			min1=temp/2;
			a[i][0]=max1;
			f[i][0]+=2*f[i-1][0];
			if(max1>min1)
			{
				a[i][1]=min1;
				f[i][0]/=2;
				f[i][1]+=f[i-1][0];
			}
			if(a[i-1][1]>0)
			{
				temp=a[i-1][1]-1;
				max2=temp-temp/2;
				min2=temp/2;
				a[i][1]=min2;
				if(max2>min2)
				{
					f[i][0]+=f[i-1][1];
					f[i][1]+=f[i-1][1];
				}
				else
				{
					f[i][1]+=2*f[i-1][1];
				}
			}
			if(ans+f[i][0]>=k)
			{
				if(a[i][0]==1)
				{
					printf("0 0\n");
				}
				else
				{
					temp=a[i][0]-1;
					printf("%lld %lld\n",temp-temp/2,temp/2);
				}
				flag=1;
				break;
			}
			ans+=f[i][0];
			if(ans+f[i][1]>=k)
			{
				if(a[i][1]==1)
				{
					printf("0 0\n");
				}
				else
				{
					temp=a[i][1]-1;
					printf("%lld %lld\n",temp-temp/2,temp/2);
				}
				flag=1;
				break;
			}	
			ans+=f[i][1];
			//printf("%lld %lld %lld %lld\n",a[i][0],a[i][1],f[i][0],f[i][1]);
			i++;
		}
		if(flag==0)
		{
			printf("0 0\n");
		}
	}
	return 0;
}
