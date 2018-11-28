#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define vec vector<long long>
#define MOD 1000000007
#define ull unsigned long long
ifstream in("row10.in");
ofstream out("row10.ans");
int main()
{	
	ll t,n,i,j,k;
	in>>t;
	for(i=1;i<=t;i++)
	{
		string s;
		ll l=s.size();
		in>>s;
		n=0;
		for(j=s.size()-2;j>=0;j--)
		{
			if(s[j]>s[j+1])
			{
				s[j]--;
				for(k=j+1;k<s.size();k++)
				s[k]='9';
			}
		}
		for(j=0;j<s.size();j++)
		{
			n=((n*10)+(s[j]-48));
		}
		out<<"Case #"<<i<<": "<<n<<endl;
	}
    
}
