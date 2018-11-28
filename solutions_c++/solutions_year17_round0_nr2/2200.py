#include <bits/stdc++.h>

using namespace std;

string s;
int T,cas;

int main()
{
	for(cin>>T;T--;)
	{
		cin>>s;
		int n=s.length();
		for(int i=1;i<n;i++)
			if(s[i]<s[i-1])
			{
				int p=i-1;
				for(;p>=0 && s[p]>=s[p+1];p--);
				for(s[++p]--,p++;p<n;s[p++]='9');
			}
		cout<<"Case #"<<++cas<<": ";
		for(int i=0,f=0;i<n;i++)
			if(f || s[i]!='0') putchar(s[i]),f=1;
		cout<<endl;
	}
}