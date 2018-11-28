#include <bits/stdc++.h>
using namespace std;
int cnt[4];
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T, no=1;
	cin>>T;
	while(T--)
	{
		memset(cnt,0,sizeof cnt);
		int n,p;
		cin>>n>>p;
		for(int i=0;i<n;i++)
		{
			int t;
			cin>>t;
			t%=p;
			cnt[t]++;
		}
		int ans=0;
		ans+=cnt[0];
		//cout<<ans<<endl;
		if(p==2)
		{
			ans+=(cnt[1]+1)/2;
		}
		else if(p==3)
		{
			ans+=min(cnt[1],cnt[2]);
			//cout<<ans<<endl;
			int t=abs(cnt[1]-cnt[2]);
			ans+=(t+2)/3;
		}
		else  //p==4
		{
			int tp=0;
			assert(ans>=tp); tp=ans;
			ans+=cnt[2]/2;
			assert(ans>=tp); tp=ans;
			ans+=min(cnt[1],cnt[3]);
			assert(ans>=tp); tp=ans;
			int t=abs(cnt[1]-cnt[3]);
			if(cnt[2]%2==0)
			{
				ans+=(t+3)/4;
			}
			else
			{
				ans+=(t+2+3)/4;
			}
			assert(ans>=tp); tp=ans;
		}
		cout<<"Case #"<<no++<<": "<<ans<<endl;
	}
}
