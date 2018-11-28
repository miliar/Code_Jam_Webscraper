#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; cin>>t;
	string s;
	int k;
	map<char, char> inv;
	inv['+'] = '-';
	inv['-'] = '+';
	for(int q=1; q<=t; q++)
	{
		cin>>s>>k;
		int n = s.size();
		int cnt=0, i;
		for(i=0; i<(n-k); i++)
		{
			if(s[i]=='-')
			{
				cnt++;
				for(int j=0; j<k; j++)
				{
					s[i+j]=inv[s[i+j]];
				}
			}
		}
		int flag=0;
		for(;i<(n-1);i++)
		{
			if(s[i]!=s[i+1])
			{
				flag = 1;
			}
		}
		if(flag==0)
		{
			if(s[n-1]=='-')	cnt++;
			cout<<"Case #"<<q<<": "<<cnt<<"\n";
		}
		else cout<<"Case #"<<q<<": IMPOSSIBLE\n";
	}
	return 0;
}