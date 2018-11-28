#include<bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define mp make_pair
#define lli long long int
#define INF 1000000000000
#define MOD 1000000007
#define FOR(name,initial,final) for(lli name=initial;name<final;name++)
#define rz resize
#define all(x) (x).begin(),(x).end()
#define T int t; cin>>t; while(t--)
using namespace std;
typedef vector<lli> vli;
typedef pair<lli,lli> pi;
typedef pair<pair<lli,lli>,lli> ppi;
typedef vector<vector<lli> > vv;
int main()
{
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		string s;
		lli k;
		cin>>s>>k;
		int len = s.length();
		vector<bool> v(len);

		FOR(i,0,len)
		{
			if(s[i]=='-')
				v[i]=false;
			else
				v[i]=true;
		}
		lli ans=0;
		FOR(i,0,len-k+1)
		{
			if(!v[i])
			{
				ans++;
				FOR(j,i,i+k)
				{
					v[j]=!v[j];
				}
			}
		}
		bool f=false;
		FOR(i,0,len)
		{
			if(!v[i])
			{
				f=true;
				break;
			}
		}
		if(f)
		{
			cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<test<<": "<<ans<<endl;
		}


	}
}