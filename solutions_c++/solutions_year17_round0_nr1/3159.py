#include<bits/stdc++.h>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<list>
#include<map>
#define ll long long
#define INF 2000000000
#define NINF -2000000000
#define MOD 1000000007
#define br '\n'
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		char a[1001];
		int k;
		cin>>a>>k;
		int l=strlen(a);
		int ans=0;
		bool flag=true;
		for(int i=0;i<l;i++)
		{
			if(a[i]=='-')
			{
				if(i+k>l)
				{
					flag=false;
					break;
				}
				else
				{
					ans++;
					for(int j=i;j<i+k;j++)
					{
						if(a[j]=='+')
							a[j]='-';
						else
							a[j]='+';
					}
				}
			}
		}
		cout<<"Case #"<<tc<<": ";
		if(flag==false)
			cout<<"IMPOSSIBLE"<<br;
		else
			cout<<ans<<br;
	}
	return 0;
}

