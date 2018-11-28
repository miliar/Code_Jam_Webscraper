#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define vec vector<long long>
#define MOD 1000000007
#define ull unsigned long long
int main()
{
	ull t,i,j,k,kk;
    ifstream in("row10.in");
    ofstream out("row10.ans");
    in>>t;
    for(i=1;i<=t;i++)
    {
		string s;
		in>>s;
		in>>kk;
		ll ans=0;
		for(j=0;j<=s.size()-kk;j++)
		{
			if(s[j]=='-')
			{
				ans++;
				for(k=j;k<j+kk;k++)
				{
					if(s[k]=='-')
					s[k]='+';
					else
					s[k]='-';
				}
			}
		}
		for(j=s.size()-kk;j<s.size();j++)
		if(s[j]=='-')
		{
			ans=-1;
			break;
		}
		if(ans==-1)
		out<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		else
		out<<"Case #"<<i<<": "<<ans<<endl;
    }
}
