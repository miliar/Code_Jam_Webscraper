#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int cnt=1;
	while(t--)
	{
		string s;
		int k;
		cin>>s>>k;
		cout<<"Case #"<<cnt<<": ";
		cnt++;
		int ans=0;
		int n=s.size();
		for(int i=n;i>=(k-1);i--)
		{
			if(s[i]=='-')
			{
				for(int j=i;j>(i-k);j--)
					if(s[j]=='+')
						s[j]='-';
					else s[j]='+';
				ans++;
			}
		}
		bool posi=true;
		for(int i=0;i<n;i++)
			if(s[i]!='+')
				posi=false;
		if(!posi)
			cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;

	}
	return 0;
}
