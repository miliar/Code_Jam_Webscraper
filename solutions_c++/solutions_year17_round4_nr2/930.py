#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
main()
{
	int t;cin>>t;
	for(int count=1;count<=t;count++)
	{
		int n,c,m;cin>>n>>c>>m;
		int cnt[3][1010]={},cntman[3]={},p[1010],b[1010],M=0;
		for(int i=0;i<m;i++)
		{
			cin>>p[i]>>b[i];
			cnt[b[i]-1][p[i]-1]++;
			M=max(M,++cntman[b[i]-1]);
		}
		int ans=max(M,cnt[0][0]+cnt[1][0]);
		M=ans-cnt[0][0]-cnt[1][0];
		int plus=0;
		for(int i=1;i<n;i++)
		{
			int now=cnt[0][i]+cnt[1][i];
			if(now<=ans)
			{
				M+=ans-now;
			}
			else
			{
				now-=ans;
				plus+=now;
				if(M>=now)
				{
					M-=now;
				}
				else
				{
					now-=M;
					M=0;
					int l=(now+i-1)/i;
					ans+=l;
					now-=l*i;
					M-=now;
				}
			}
		}
		cout<<"Case #"<<count<<": "<<ans<<" "<<plus<<endl;
	}
}
