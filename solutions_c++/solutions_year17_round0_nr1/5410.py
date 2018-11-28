#include<bits/stdc++.h>
using namespace std;

bool check(string s)
{
	for (int i = 0;i<s.size();i++)
	{
		if (s[i]=='-') return false;
	}
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t; cin>>t;
	for (int j = 1;j<=t;j++)
	{
		string s; int k; cin>>s>>k;
		string s1 = s;
		int ans = INT_MAX;
		int c = 0;
		for (int i = 0;i<s.size();i++)
		{
			if (s1[i]=='-' && s.size()-i>=k)
			{
				for(int x = 0;x<k;x++) 
				{
					if (s1[i+x]=='+') s1[i+x] = '-';
					else s1[i+x] = '+'; 
				}
				c++;
			}
		}
		if (check(s1)) ans = min(ans,c);
		c = 0; string s2 = s;
		for (int i= s.size()-1;i>=0;i--)
		{
			if (s2[i]=='-' && i+1>=k)
			{
				for (int x = 0;x<k;x++) 
				{
					if (s2[i-x]=='+') s2[i-x] = '-';
					else s2[i-x] = '+';
				}
				c++;
			}
		}
		if (check(s2)) ans = min(ans,c);
		if (ans==INT_MAX) cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}

