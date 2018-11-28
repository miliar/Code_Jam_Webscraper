#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define X first
#define Y second
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
#define forn(n) for(ll i=0;i<n;i++)
#define forin(n1,n2) for(ll i=n1;i<n2;i++)
using namespace std;
typedef pair<int,int>pii;
FILE *ptr=freopen("in.txt","r",stdin);
FILE *ptr1=freopen("out.txt","w",stdout);
int main()
{
	ll tc;
	cin>>tc;
	for(int k=1;k<=tc;k++)
	{
		string s;cin>>s;
		if(s.length()==1) cout<<"Case #"<<k<<": "<<s<<"\n";
		else
		{
			ll t=s[0]-'0';
			int i=1;
			for(i=1;i<s.length();i++)
			{
			if((s[i]-'0')>=t)
			{
				t=s[i]-'0';
			}
			else break;
			}
			if(i!=s.length())
			{
				for(int p=i;p<s.length();p++) s[p]='9';
				i--;
				while(i>0&&s[i-1]==s[i])
				{
					s[i]='9';
					i--;
				}
				s[i]-=1;
			}
			if(s[0]=='0') cout<<"Case #"<<k<<": "<<s.substr(1,s.length()-1)<<"\n";
			else cout<<"Case #"<<k<<": "<<s<<"\n";
		}
	}
	return 0;
}

