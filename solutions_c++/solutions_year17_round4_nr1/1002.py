#include<iostream>
#include<algorithm>
using namespace std;
main()
{
	int t;cin>>t;
	for(int count=1;count<=t;count++)
	{
		int n,p;cin>>n>>p;
		int G[100];
		for(int i=0;i<n;i++)
		{
			cin>>G[i];
			G[i]%=p;
		}
		int cnt[4]={};
		for(int i=0;i<n;i++)
		{
			cnt[G[i]]++;
		}
		int ans=cnt[0];
		if(p==2)
		{
			ans+=cnt[1]/2;
			ans+=cnt[1]%2;
		}
		else if(p==3)
		{
			int now=min(cnt[1],cnt[2]);
			ans+=now;
			cnt[1]-=now,cnt[2]-=now;
			ans+=cnt[1]/3;
			ans+=cnt[2]/3;
			if(cnt[1]%3||cnt[2]%3)ans++;
		}
		else
		{
			int now=min(cnt[1],cnt[3]);
			ans+=now;
			cnt[1]-=now,cnt[3]-=now;
			if(cnt[1])
			{
				if(cnt[1]/2>=cnt[2])
				{
					ans+=cnt[2];
					cnt[1]-=cnt[2]*2;cnt[2]=0;
				}
				else
				{
					if(cnt[1]/2>cnt[2]/2)
					{
						ans+=now=cnt[1]/2;
						cnt[1]-=now*2,cnt[2]-=now;
						ans+=now=cnt[2]/2;
						cnt[2]-=now*2;
					}
					else
					{
						ans+=now=cnt[2]/2;
						cnt[2]-=now*2;
						if(cnt[2]&&cnt[1]>1)
						{
							ans++;cnt[2]=0;cnt[1]-=2;
						}
					}
				}
				ans+=now=cnt[1]/4;
				cnt[1]-=now*4;
			}
			else if(cnt[3])
			{
				if(cnt[3]/2>=cnt[2])
				{
					ans+=cnt[2];
					cnt[3]-=cnt[2]*2;cnt[2]=0;
				}
				else
				{
					if(cnt[3]/2>cnt[2]/2)
					{
						ans+=now=cnt[3]/2;
						cnt[3]-=now*2,cnt[2]-=now;
						ans+=now=cnt[2]/2;
						cnt[2]-=now*2;
					}
					else
					{
						ans+=now=cnt[2]/2;
						cnt[2]-=now*2;
						if(cnt[2]&&cnt[3]>1)
						{
							ans++;cnt[2]=0;cnt[3]-=2;
						}
					}
				}
				ans+=now=cnt[3]/4;
				cnt[3]-=now*4;
			}
			else
			{
				ans+=now=cnt[2]/2;
				cnt[2]-=now*2;
			}
			if(cnt[1]||cnt[2]||cnt[3])ans++;
		}
		cout<<"Case #"<<count<<": "<<ans<<endl;
	}
}
