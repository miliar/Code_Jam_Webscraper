#include<bits/stdc++.h>
using namespace std;
#define int long long
#define double long double 
#define mp make_pair
#define pb push_back
#define f first
#define s second
int k;
string good,bad;
int rec(string s)
{
	if (s.length()==k)
	{
		if (s==bad) return 1;
		else if (s==good)return 0;
		return -1e9;
	}
	if (s[0]=='-')
	{
		for (int i=0;i<k;i++)
		{
			if (s[i]=='-') s[i]='+';
			else s[i]='-';
		}
		return rec(s.substr(1,s.length()-1))+1;
	}
	return rec(s.substr(1,s.length()-1));
}
signed main() 
{
    int t;
    cin>>t;
    int now=1;
    ofstream out("output.txt");
    while (t--)
    {
    	string s;
    	cin>>s;
    	cin>>k;
    	for (int i=0;i<k;i++)
    	{
    		good+='+';
    		bad+='-';
		}
		out<<"Case #"<<now++<<": ";
    	if (rec(s)>=0)
    	{
    		out<<rec(s);
		}
		else 
		{
			out<<"IMPOSSIBLE";
		}
		good.clear();
		bad.clear();
		out<<"\n";
	}
    return 0;
} 
