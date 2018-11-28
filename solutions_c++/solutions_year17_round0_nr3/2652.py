#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;
int main()
{
	int t,i;
	bool flag;
	cin>>t;
	long long n,k,ch,ans1,ans2;
	pair<long long,long long > bg,sm,tmp1,tmp2;
	for(i=1;i<=t;i++)
	{
		ch=1;
		flag=0;
		cin>>n>>k;
		bg.f=n;
		bg.s=1;
		while(k>ch)
		{
			k-=ch; 
			ch*=2; 
			if(flag)
			{
				if((long long)(bg.f/(long long)2)==(long long)(sm.f/(long long)2))
				{
					if(bg.f%2==0)
					{
						bg.f=bg.f/(long long)2;
						bg.s=bg.s+(sm.s*(long long)2);
						sm.f=bg.f-(long long)1;
						sm.s=bg.s;
					}
					else
					{
						bg.f=sm.f/(long long)2;
						bg.s=sm.s+(bg.s*(long long)2);
						sm.f=bg.f-(long long)1;
						sm.s=sm.s;
					}
				}
				else
				{
					if(bg.f%2==0)
					{
						bg.f=bg.f/(long long)2;
						bg.s=bg.s;
						sm.f=bg.f-(long long)1;
						sm.s=bg.s+(sm.s*(long long)2);
					}
					else
					{
						bg.f=sm.f/(long long)2;
						sm.s=(bg.s*(long long)2)+sm.s;
						bg.s=sm.s;
						sm.f=bg.f-(long long)1;
					}
				}
			}
			else
			{
				if(bg.f%2==0)
				{
					bg.f=bg.f/(long long)2;
					bg.s=bg.s;
					sm.f=bg.f-(long long)1;
					sm.s=bg.s;
					flag=1;
				}
				else
				{
					bg.f=bg.f/(long long)2;
					bg.s=bg.s*(long long)2;
				}
			}
		}
		if(k<=bg.s)
		{
			if(bg.f%2==0)
			{
				ans1=bg.f/(long long)2;
				ans2=ans1-(long long)1;
			}
			else
			{
				ans1=bg.f/(long long)2;
				ans2=ans1;
			}
		}
		else
		{
			if(sm.f%2==0)
			{
				ans1=sm.f/(long long)2;
				ans2=ans1-(long long)1;
			}
			else
			{
				ans1=sm.f/(long long)2;
				ans2=ans1;
			}
		}
		cout<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<"\n";
	}
	return 0;
}
