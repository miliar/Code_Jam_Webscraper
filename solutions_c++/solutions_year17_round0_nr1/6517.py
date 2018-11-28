#include<bits/stdc++.h>
#define pb push_back
using namespace std;
int main()
{
	int i,j,tc,ans,flag;
	string s;
	vector<int>v;
	cin>>tc;
	for(int k=1;k<=tc;++k)
	{
		ans=0,flag=1;
		cin>>s>>i;
		v.clear();
		for(j=0;j<s.size();++j)
		{
			if(s[j]=='-')
			v.pb(j+1);
		}
		while(!v.empty())
		{   
			if((v.at(0)+i-1)>s.size())
			{
				flag=0;
				break;
			}
			else
			{
				int f=v[0];
			
				for(j=f;j<f+i;++j)
				{
					auto r=find(begin(v),end(v),j);
					if(r!=end(v))
					v.erase(r);
					else
					v.pb(j);
				
				}	++ans;
				sort(v.begin(),v.end());
			}
		}
		if(flag==0)
			cout<<"Case #"<<k<<": IMPOSSIBLE"<<"\n";
		else
			cout<<"Case #"<<k<<": "<<ans<<"\n";
	}
	return 0;
}