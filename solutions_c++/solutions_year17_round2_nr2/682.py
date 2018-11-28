#include <bits/stdc++.h>
using namespace std;
char name[]="ROYGBV";
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T, no=1;
	cin>>T;
	while(T--)
	{
		//clog<<no<<endl;
		int n;
		cin>>n;
		int cnt[6];
		for(int i=0;i<6;i++)
			cin>>cnt[i];
		pair<int,char> ccnt[3];
		for(int i=0;i<3;i++)
			ccnt[i]={cnt[i*2],name[i*2]};
		sort(ccnt,ccnt+3);
		if(ccnt[0].first+ccnt[1].first>=ccnt[2].first)
		{
			string seq;
			for(int i=0;i<ccnt[1].first-ccnt[0].first;i++)
			{
				seq+=ccnt[1].second;
			}
			for(int i=0;i<ccnt[0].first;i++)
			{
				seq+=ccnt[0].second;
				seq+=ccnt[1].second;
			}
			string ans;
			for(int i=0;i<seq.size();i++)
			{
				if(i<ccnt[2].first)
					ans+=ccnt[2].second;
				ans+=seq[i];
			}
			cout<<"Case #"<<no++<<": "<<ans<<endl;
			assert(ans.size()==n);
			//clog<<". "<<n<<endl;
			for(int i=0;i<n;i++)
			{
				//clog<<i<<endl;
				assert(ans[i]!=ans[(i+1)%n]);
			}
		}
		else
		{
			cout<<"Case #"<<no++<<": IMPOSSIBLE"<<endl;
		}
	}
}