#include<bits/stdc++.h>
 
#define MOD 	1000000007
#define ll 		long long
#define	inf		1e12
#define MAX		10000000
#define pii		pair<int, int>
#define F 		first
#define S 		second
 
using namespace std;



int main()
{
	
	int t, n, k, ans, imp;
	string s;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		cin>>s;
		cin>>k;
		n = (int)s.length();
		ans = 0;
		imp = 0;
		for(int i=0;i<=n-k;i++)
		{
			if(s[i] == '-')
			{
				ans++;
				for(int j=i;j<i+k;j++)
				{
					if(s[j] == '-')
						s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			if(s[i] == '-')
			{
				imp = 1;
				break;
			}
		}
		cout<<"Case #"<<test<<": ";
		if(imp)
			cout<<"IMPOSSIBLE";
		else cout<<ans;
		if(test!=t)
			cout<<endl;
	}
	return 0;
}