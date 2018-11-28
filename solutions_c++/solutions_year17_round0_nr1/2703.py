#include <bits/stdc++.h>
using namespace std;

#define cr(x) cerr<<#x<<"= "<<x<<'\n'
#define int long long

typedef pair <int, int > pii;

int32_t main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int t;
	cin>>t;
	for(int tcnt=1;tcnt<=t;tcnt++)
	{
		string s;
		int n, k, ans=0;
		cin>>s>>k;
		n=(int)s.size();
		for(int i=0;i<n-k+1;i++)
			if(s[i]=='-')
			{
				ans++;
				for(int j=i;j<i+k;j++)
					s[j]=(s[j]=='+'? '-': '+');
			}
		bool b=0;
		for(int i=n-k+1;i<n;i++)
			if(s[i]=='-')
			{
				cout<<"Case #"<<tcnt<<": IMPOSSIBLE"<<'\n';
				b=1;
				break;
			}
		if(!b) cout<<"Case #"<<tcnt<<": "<<ans<<'\n';
	}
}
