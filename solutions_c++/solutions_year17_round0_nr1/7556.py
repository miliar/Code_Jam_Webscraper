#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int ar[1001];
int main()
{
	int t ;
	cin>>t;
	int m =1;
	while(t--)
	{
		string st;
		cin>>st;
		int k;
		cin>>k;
		int n = st.size();
		int i,j;
		for(i=0;i<n;i++)
			ar[i]=0;
		int fl=0;
		int don = 0;
		int cur = -1000000;
		int ans = 0;
		for(i=0;i<=n-k;i++)
		{
			if(st[i]=='-')
			{
				ans++;
				for(j=i;j<i+k;j++)
				{
					if(st[j]=='-')
						st[j]='+';
					else
						st[j]='-';
				}
			}
		}
		for(i=0;i<n;i++)
		{
			if(st[i]=='+')
				don++;
		}
		cout<<"Case #"<<m<<": ";
		if(don!=n)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<ans<<endl;
		m++;
	}
	return 0;
}
