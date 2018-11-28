#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int t;
	cin>>t;
	for(int a=1; a<=t; a++)
	{
		string s;
		int k, c=0;
		cin>>s>>k;
		for(int i=0; i<s.length()-k+1; i++)
			if(s[i]=='-')
			{
				c++;
				for(int j=0; j<k; j++)
					s[i+j] = s[i+j] == '+' ? '-' : '+';
			}
		bool possible = true;
		for(int i=s.length()-k; i<s.length(); i++)
			if(s[i]=='-')
				possible = false;
		cout<<"Case #"<<a<<": ";
		if(possible)
			cout<<c<<'\n';
		else
			cout<<"IMPOSSIBLE"<<'\n';
	}
}
