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
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		ll n;
		cin>>n;
		ll a[20];
		ll temp=n,l=0;
		while(temp)
		{
			a[l++]=temp%10;
			temp/=10;
		}
		for(int i=1;i<l;i++)
		{
			if(a[i]>a[i-1])
			{
				a[i]--;
				for(int j=i-1;j>=0;j--)
				{
					a[j]=9;
				}
			}
		}
		ll ans=0;
		for(int i=l-1;i>=0;i--)
		{
			ans=(ans*10)+a[i];
		}
		cout<<"Case #"<<tc<<": ";
		cout<<ans<<br;
	}
	return 0;
}

