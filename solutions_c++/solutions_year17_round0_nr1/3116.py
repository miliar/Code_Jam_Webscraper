#include <iostream>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T, no=0;
	cin>>T;
	while(T--)
	{
		string s;
		int k;
		cin>>s>>k;
		int ans=0;
		for(int i=0;i<s.size()-k+1;i++)
		{
			if(s[i]=='-')
			{
				ans++;
				for(int j=i;j<=i+k-1;j++)
					s[j]=(s[j]=='-'?'+':'-');
			}
		}
		for(int i=0;i<s.size();i++)
			if(s[i]=='-')
				ans=-1;
		cout<<"Case #"<<++no<<": ";
		if(ans>=0)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
}