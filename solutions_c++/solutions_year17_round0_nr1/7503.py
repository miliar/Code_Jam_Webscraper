#include<bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	int t, k;
	string s;
	cin>>t;

	for(int tc = 1; tc <= t; tc++)
	{
		cin>>s>>k;
		int n = s.length(), ans = 0;
		for(int i = 0; i < n-k+1; i++)
		{
			if(s[i] == '-')
			{
				ans++;
				for(int j = 0; j < k; j++)
					s[i+j] = (s[i+j] == '+' ? '-' : '+');
			}
		}
		int flag = 1;
		cout<<"Case #"<<tc<<": ";
		for(int i = 0; i < n; i++)
		{
			if(s[i] == '-')
				flag = 0;
		}
		if(flag)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}

	return 0;
}