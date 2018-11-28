#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("Input.txt","r",stdin);
	freopen("Output.out","w",stdout);
	int t,z=1;
	cin>>t;
	while(t--)
	{
		int k;
		char s[1050];
		cin>>s>>k;
		//cout<<s<<endl;
		int n=strlen(s),ct=0,ct1=0;
		for(int i=0;i+k<=n;i++)
		{
			if(s[i]=='+')
				continue;
			ct++;
			int fl=0,newpos;
			for(int j=0;j<k;j++)
			{
				if(s[i+j]=='+')
					s[i+j]='-';
				else
					s[i+j]='+';
				if(s[i+j]=='-'&&fl==0)
				{
					fl=1;
					newpos=i+j;
				}
			}
			if(fl==1)
				i=newpos-1;
		}

		for(int i=0;i<n;i++)
			if(s[i]=='+')
				ct1++;
			//cout<<s<<endl;
		printf("Case #%d: ",z++);
		if(ct1==n)
			cout<<ct<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}