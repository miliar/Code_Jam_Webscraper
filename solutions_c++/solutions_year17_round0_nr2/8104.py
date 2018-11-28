#include<iostream>
#include<cstdio>
int main()
{
	long long t,n,a[100],k=0,i,f,ans,t1=0,j;
	FILE *f1=freopen("B-large.in","r",stdin);
	FILE *f2=freopen("OUTPUT_3.txt","w",stdout);
	scanf("%lld",&t);
	while(t--)
	{
		t1++;
		k=0;
		scanf("%lld",&n);
		while(n>0)
		{
			a[k++]=n%10;
			n=n/10;
		}
		f=0;
		for(i=k-1;i>0;i--)
		{
			if(a[i]>a[i-1])
			{
				f=1;
				a[i]--;
				for(j=i-1;j>=0;j--)
				{
					a[j]=9;
				}
				for(j=i;j<k-1;j++)
				{
					if(a[j]<a[j+1])
					{
						a[j]=9;
						a[j+1]--;
					}
				}
				break;
			}
		}
		ans=0;
		for(i=k-1;i>=0;i--)
		{
			if(i==k-1)
			{
				if(a[i]>0)
				{
					ans=ans*10+a[i];
				}
			}
			else
			{
				ans=ans*10+a[i];
			}
		}
		printf("Case #%lld: %lld\n",t1,ans);
	}
	fclose(f1);
	fclose(f2);
	return 0;
}
