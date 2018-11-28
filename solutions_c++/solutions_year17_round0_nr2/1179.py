#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int main()
{
	int T,st,ed,n;
	string s;
	scanf("%d",&T);
	for(int I=1;I<=T;I++)
	{
		cin>>s;
		n=s.length();
		st=0;	ed=n;
		for(int i=1;i<n;i++)
			if(s[i-1]<s[i])
				st=i;
			else if(s[i-1]>s[i])
			{
				ed=i;
				break;
			}

		if(ed!=n)
		{
			s[st]=s[st]-1;
			for(int i=st+1;i<n;i++)
				s[i]='9';
			if(s[0]=='0')
				s.erase(s.begin());
		}
		printf("Case #%d: ",I);
		cout<<s<<endl;
		
	}
}