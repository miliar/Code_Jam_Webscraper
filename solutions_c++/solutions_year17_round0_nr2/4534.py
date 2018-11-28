#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
	int t,tc=1;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		int n = s.length();
		int j,i = n-1;
		while(i>0)
		{
			if(s[i] < s[i-1]){
				s[i-1]--;
				for(j=i ; j<n ; j++) 
					s[j]='9';
			}
			i--;
		}
		i=0;
		while(s[i]=='0')
			i++;
		cout<<"Case #"<<tc++<<": "; 
		for(j=i ; j<n ; j++)
			cout<<s[j];
		cout<<"\n";
	}
	return 0;
} 