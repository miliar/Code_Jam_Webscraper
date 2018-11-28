using namespace std;
#include <bits/stdc++.h>
#define pb push_back
#define ll long long
#define ull unsigned long long 
#define FF first
#define SS second
#define MOD 1000000007

typedef vector<ll> vll;


int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int tt=0;tt<t;tt++)
	{
		string s;
		cin>>s;
		ll ans = 0;
		int n = s.size();
		int k;cin>>k;
		for(int i=0;i<n-k+1;i++)
		{
			if(s[i]=='-')
			{
				ans++;
				for(int j=0;j<k;j++)
				{
					if(s[i+j]=='+')
					{
						s[i+j]='-';
					}
					else
					{
						s[i+j]='+';
					}
				}
			}
		}
		int flag=0;
		for(int i=0;i<n;i++)
		{
			if(s[i]=='-')flag=1;
		}
		if(!flag)
		{
			cout<<"Case #"<<tt+1<<": "<<ans<<endl;
		}
		else
		{
			cout<<"Case #"<<tt	+1<<": "<<"IMPOSSIBLE"<<endl;	
		}



	}
}	
