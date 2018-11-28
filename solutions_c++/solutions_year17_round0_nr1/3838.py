#include <bits/stdc++.h>
using namespace std;
#define ll int
#define N ((ll)2010)

ll t,k;
bool changed[N];
string s;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);
	fin>>t;
	for(int i=1;i<=t;i++)
	{
		ll res=0;
		bool now=0,flg=0;
		memset(changed,0,sizeof changed);
		fin>>s>>k;
		for(int i=0;i<s.size();i++)
		{
			bool ok=(s[i]=='+');
			if(i-k>=0)now^=changed[i-k];
			if(!(ok^now))
			{
				if((ll)s.size()-i<k)
				{
					flg=1;
					break;
				}
				res++;changed[i]=1;now^=1;	
			}
		}
		fout<<"Case #"<<i<<": ";
		if(flg)fout<<"IMPOSSIBLE\n";
		else fout<<res<<"\n";
	}
	return 0;
}
