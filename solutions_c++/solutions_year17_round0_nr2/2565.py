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
string dec(string s,int i)
{
	if(s[i]-'0'>0)
	{
		if(i==0)
			s[i]=s[i]-1;
		else
		{
			if(s[i]==s[i-1])
			{
				s[i]='9';
				s=dec(s,i-1);
			}
			else
			{
				s[i]=s[i]-1;
			}
		}
		return s;
	}
	else
	{
		s[i]='9';
		s=dec(s,i-1);
		return s;
	}
}
int main()
{
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		string n;
		cin>>n;
		int len = n.length();
		if(len==1)
		{
			cout<<"Case #"<<test<<": "<<n<<endl;
		}
		else
		{
			bool all=false;
			FOR(i,0,len-1)
			{
				if(n[i+1]<n[i])
				{
					if(!all)
					{
						n=dec(n,i);
						n[i+1]='9';
						all=true;
					}
					else
					{
						n[i+1]='9';
					}
				}
			}
			cout<<"Case #"<<test<<": ";
			bool first=true;
			FOR(i,0,len)
			{
				if(n[i]=='0' && first)
				{
					continue;
				}
				else
				{
					cout<<n[i];
					first=false;
				}
				
			}
			cout<<endl;
		}
	}

}