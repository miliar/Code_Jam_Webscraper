#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int t,ans,f,l,k;
	string s;
	cin>>t;
	for(int loop=1;loop<=t;loop++)
	{
		ans=f=0;
		cin>>s>>k;
		l=s.length();
		for(int i=0;i<=l-k;i++)
			if(s[i] == '-')
			{
				ans++;
				for(int j=i;j<i+k;j++)
				{
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		for(int i=0;i<l;i++)
			if(s[i] == '-')
			{
				f=1;
				break;
			}
		if(f)
			cout<<"Case #"<<loop<<": IMPOSSIBLE\n";
		else
			cout<<"Case #"<<loop<<": "<<ans<<"\n";
	}
	return 0;
}