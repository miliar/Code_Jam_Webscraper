#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll a[20],t,d,n;

int main()
{
	ll i,j,k,ans,p=0;
	scanf("%lld",&t);
	while(t--)
	{
		p++;
		scanf("%lld",&n);
		k=n;
		d=0;
		while(k>0)
		{
			a[d++]=k%10;
			k/=10;	
		}
		
		//for(i=0;i<d;i++)
		//    cout<<a[i];
		//cout<<endl;
		for(i=0;i<d-1;i++)
		{
		    //cout<<a[i]<<endl;
			for(j=i;j<d-1;j++)
			{
				if(a[j]<a[j+1])
					break;
			}
			if(j==d-1)
				break;
			else
			{
				a[i]=9;
				a[i+1]--;	
			}	
		}
		ans=0;
		for(i=d-1;i>=0;i--)
			ans=ans*10+a[i];
		printf("Case #%lld: %lld\n",p,ans);
	}
	return 0;
}
