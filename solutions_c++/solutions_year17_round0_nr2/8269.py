#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
	// your code goes here
	
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t, it;
	cin>>t;
	for(it=1; it<=t; it++)
	{
		string s;
		cin>>s;
		int i, n=s.size(), j;
		int c=0;
		for(i=0; i<n-1; i++)
		{
			if(s[i]==s[i+1])
				c++;
			else if(s[i]<s[i+1])
				c=0;
			else if(s[i]>s[i+1])
			{
				int x=int(s[i-c])-48;
				s[i-c]=x+47;
				for(j=i-c+1; j<n; j++)
					s[j]='9';
			}
		}

		cout<<"Case #"<<it<<": ";
		if(s[0]!='0')
			cout<<s[0];
		for(i=1; i<n; i++)
			cout<<s[i];
		cout<<"\n";
	}
	
	return 0;
}
