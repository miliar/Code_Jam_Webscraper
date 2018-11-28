#include"bits/stdc++.h"
#define fast ios_base::sync_with_stdio(false);cin.tie(0);
#define pb push_back
#define mp make_pair
#define ll long long int
#define vi vector<int>
#define vii vector<pair< int,int> >
#define pii pair<int,int>
#define plli pair<ll,ll>
#define ff first
#define ss second
#define MOD 1000000007
#define INF 99999999
using namespace std;
char flip(char ch)
{
	if(ch=='-')
	return '+';
	return '-';
}
int main()
{
	fast
	int t=1,cases=0;
	cin>>t;
	while(t--)
	{
		int i,j,k;
		cases++;
		string s;
		cin>>s>>k;
		int ans=0;
		for(i=0;i<=s.size()-k;i++)
		{
			if(s[i]=='-')
			{
				ans++;
				for(j=i;j<i+k;j++)
				{
					s[j]=flip(s[j]);
				}
			}
		}
		bool ok=true;
		for(i=0;i<s.size();i++)
		{
			if(s[i]=='-')
			ok=false;
		}
		if(ok)
		cout<<"Case #"<<cases<<": "<<ans<<"\n";
		else
		cout<<"Case #"<<cases<<": "<<"IMPOSSIBLE"<<"\n";
	}
}