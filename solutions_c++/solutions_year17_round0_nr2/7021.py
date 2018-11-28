#include<bits/stdc++.h>
using namespace std;
#define int long long
#define double long double 
#define mp make_pair
#define pb push_back
#define f first
int k;
string good,bad;
string rec(string s)
{
	for (int i=s.length()-1;i>0;i--)
	{
		if (s[i]<s[i-1])
		{
			s[i-1]--;
			for (int j=s.length()-1;j>=i;j--)
			{
				s[j]='9';
			}
		}
	}
	while (s.length()>0&&s[0]=='0')
	{
		if (s[0]=='0')
		{
			s=s.substr(1,s.length()-1);
		}
	}
	return s;
}
signed main() 
{
    int t;
    cin>>t;
    ofstream out("output.txt");
    int now=1;
    while (t--)
    {
    	string s;
	    cin>>s;
		out<<"Case #"<<now++<<": "<<rec(s);
		out<<"\n";
	}
    return 0;
} 

