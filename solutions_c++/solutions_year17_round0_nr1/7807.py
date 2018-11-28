#include<bits/stdc++.h>

typedef long long LL;  
using namespace std;

#define fillchar(a, x) memset(a, x, sizeof(a))
#define MP make_pair
#define PB push_back
#define endl '\n'

const int M = (int)1e9+7;

int main()
{
//ios_base::sync_with_stdio(0); 
	cout.precision(15);
	cout.setf(ios::fixed);

	int t;
	cin >> t;

	for(int x=0;x<t;x++)
	{
		string s;
		int k;
		cin >> s >> k;

		int ans = 0;
		int n = s.size();

		for(int i=0;i<n-k+1;i++)
		{
			if(s[i]=='-')
			{
				for(int j=0;j<k;j++)
					s[i+j] = (s[i+j]=='+' ? '-' : '+');
			ans++;	
			}	
		}

		for(int i=0;i<n;i++)
			if(s[i]=='-')
				ans = -1;

		if(ans==-1)
			cout<<"Case #"<<x+1<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<x+1<<": "<<ans<<endl;

	}	


}
