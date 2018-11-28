#include <bits/stdc++.h>
typedef long long ll;
#define MOD 1000000007
using namespace std;
int main()
{
	ios::sync_with_stdio(false), cin.tie(0);
	freopen("B-large.in", "r", stdin);
	  	freopen("output.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
//		long long x=0;
		string s;
		cin>>s;
//		for(int i=0;i<s.size();i++)
//		{
//			x*=10;
//			x+=(s[i]-'0');
//		}
		for(int i=s.size()-1,j=0;i>0;i--,j++)
		{
			if(s[i]<s[i-1])
			{
				s[i-1]--;
				for(int k=i;k<s.size();k++)
				{
					s[k]='9';
				}
			}
		}
		int x=0;
		if(s[0]=='0')
		{
			x=1;
		}
		cout<<"Case #"<<t<<": ";
		for(;x<s.size();x++)
		{
			cout<<s[x];
		}
		cout<<endl;
	}
	return 0;
}


