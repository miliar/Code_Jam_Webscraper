#include<bits/stdc++.h>
using namespace std;

int main()
{
	ifstream cin("gcj_1l.in");
	ofstream cout("gdc_1lo.txt");
	
	int i,j,k,l,m,n,id=1,t,ans;
	string str;
	cin>>t;
	while(t--)
	{
		cin>>str>>k;
		l=str.length();
		ans=0;
		for(i=0;i<l;i++)
		{
			
			if(str[i]=='+')
			continue;
			if((i+k)>l)
			break;
			ans++;
			for(j=0;j<k;j++)
			{
				if(str[i+j]=='+')
				  str[i+j]='-';
				else
				str[i+j]='+';
			}
		}
		cout<<"Case #"<<id++<<": ";
		if(i<l)
		cout<<"IMPOSSIBLE"<<endl;
		else
		cout<<ans<<endl;
	}
	
}
