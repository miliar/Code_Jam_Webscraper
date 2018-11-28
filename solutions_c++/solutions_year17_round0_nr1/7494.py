#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define mp make_pair
#define pb push_back
#define scan(x) scanf("%lld",&x)
#define MAX 100005
#define INF 1000000000000000007ll
#define mod 1000000007
#define pii pair<int,int>
#define hashmod 300007
#define hashmod1 300023

int main()
{
	freopen("C:\\Users\\watson\\Documents\\A-large.in","r",stdin);
	freopen("C:\\Users\\watson\\Documents\\output.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		string s;
		int k;
		cin>>s>>k;
		char t[1005],temp[1005];
		int ans=0;

		for(int i=0;i<s.length();i++)
			t[i]=s[i];

		for(int i=0;i<=s.length()-k;i++)
		{
			
			if(t[i]=='-')
			{
				ans++;
			for(int j=i;j<i+k;j++)
			{
				if(t[j]=='-')
					t[j]='+';
				else
					t[j]='-';
			}

			}
			
		}

		int f=0;
		for(int i=0;i<s.length();i++)
		{
			
			if(t[i]=='-')
			{
				f=1;
				break;
			}
		}
		
		if(f==0)
			cout<<"Case #"<<T<<": "<<ans<<"\n";
		else
			cout<<"Case #"<<T<<": "<<"IMPOSSIBLE"<<"\n";
}
}