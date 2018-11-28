#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	map < char, char > m;
	m['-']='+', m['+']='-';
	
	for(int c=1; c<=t; c++)
	{
		string s;
		int k;
		cin>>s>>k;
		
		int r=0;
		
		for(int i=0; i<=s.size()-k; i++)
		{
			if(s[i]=='-')
			{
				r++;
				for(int j=i; j<i+k; j++)	s[j]=m[s[j]];
			}
		}
		
		bool ok=true;
		for(int i=0; i<s.size(); i++)	if(s[i]=='-')	ok=false;
		
		cout<<"Case #"<<c<<": ";
		if(ok)	cout<<r<<endl;
		else	cout<<"IMPOSSIBLE\n";
	}
	
	return 0;
}