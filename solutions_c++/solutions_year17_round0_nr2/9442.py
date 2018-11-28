#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large2.out","w",stdout);
	
	int t;
	scanf("%d",&t);
	int z=1;
	while(t--)
	{
		long long int n;
		scanf("%lld",&n);
		int a[20],i=0;
		stack<int>s;
		while(n)
		{
			int temp=n%10;
			s.push(temp);
			n/=10;
		}
		while(s.empty()==false)
		{
			a[i++]=s.top();
			s.pop();
		}
		int len=i;
		int j=0,k;
		for(i=1;i<len;i++)
		{
			if(a[i]>a[j])
			{
				j++;
			}
			else if(a[i]<a[j])
			{
				a[j]=a[j]-1;
				for(k=j+1;k<len;k++)
				a[k]=9;
				break;
			}
			else
			{
				while(a[i]==a[j])
				i=i+1;
				if(a[i]<a[j])
				{
					a[j]=a[j]-1;
					for(k=j+1;k<len;k++)
					a[k]=9;
				}
				else
				{
					j=i;
				}
			}
		}
		long long int ans=0;
		for(i=0;i<len;i++)
		{
			ans=ans*10+a[i];
		}
		printf("Case #%d: %lld\n",z++,ans);
		
	}
	return 0;
}
