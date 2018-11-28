#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	int t;
	cin>>t;
	for(int a=1; a<=t; a++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<a<<": ";
		bool con = true;
		while(con)
		{
			con = false;
			for(int i=0; i<s.length()-1; i++)
			{
				if(s[i]>s[i+1])
				{
					con = true;
					s[i] = s[i] - 1;
					for(int j=i+1; j<s.length(); j++)
						s[j] = '9';
					break;
				}
			}
		}
		if(s[0]=='0' && s.length() > 1)
			s = s.substr(1);
		cout<<s<<'\n';
	}
}
