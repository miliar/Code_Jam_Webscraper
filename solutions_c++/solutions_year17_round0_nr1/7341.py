#include<iostream>
#include<cstdlib>
#include<bits/stdc++.h>
#include<cstring>
using namespace std;
int main()
{
	int k,T,t=0;
	cin>>T;
	while(t!=T)
	{
		string s;
		cin>>s>>k;
		int l=s.length();
		int i ,j,f=0,count=0;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='+')
				continue;
			for(j=i;j<k+i;j++)
			{
				if(k+i<=l)
				{
					if(s[j]=='-')
					s[j]='+';
					else
					s[j]='-';
			
				}
				else
				{
					f=1;
				}
			}
			count++;
			if(f==1)
			{
				cout<<"Case #"<<t+1<<": IMPOSSIBLE\n";
				break;
			}
		}
		if(f==0)
			cout<<"Case #"<<t+1<<": "<<count<<endl;
			t++;
		}
return 0;
}
