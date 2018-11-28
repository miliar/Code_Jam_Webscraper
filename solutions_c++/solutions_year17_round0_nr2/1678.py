#include <bits/stdc++.h>
using namespace std;

const int MAXN=1007; 
const int MOD=1000000007; 
const int INF=2147483647;
const double EPS=1e-8;

int i,j,k,n,m,p,t,x,y,z,ans,cnt,tcase,xcase;
string s;
int a[MAXN]; 

void check(int p)
{
	if (p==0)
	{
		s[p]--;
		for (int i = 1; i < s.length(); ++i)
		{
			s[i]='9';
		}
	}
	else if (s[p]=='0' || s[p]-1<s[p-1])
	{
		check(p-1);
	}
	else
	{
		s[p]--;
		for (int i = p+1; i < s.length(); ++i)
		{
			s[i]='9';
		}
	}
}

int main()
{
#ifdef Smile
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif
	ios::sync_with_stdio(false);
	while (cin>>tcase)
	{
		xcase=0;
		while (xcase<tcase)
		{
			xcase++;
			cout<<"Case #"<<xcase<<": ";
			cin>>s;
			if (s.length()<=1)
			{
				cout<<s<<endl;
				continue;
			}
			for (int i = 1; i < s.length(); ++i)
			{
				if (s[i-1]>s[i])
				{
					check(i-1);
					break;
				}
			}
			while (s[0]=='0') s.erase(0,1);
			cout<<s<<endl;
		}	
	}
	return 0;
}