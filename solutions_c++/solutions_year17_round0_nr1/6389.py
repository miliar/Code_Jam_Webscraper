#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);	
	int t;
	cin>>t;
	for(int y=1;y<=t;y++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int cnt=0,flag=0;
		int len=(int)s.length();
		for(int z=0;z<len;z++)
		{
			if(s[z]=='-')
			{
				if((len-z)<k)
				{
					flag=1;
					break;
				}
				for(int x=0;x<k;x++)
				{
					if(s[z+x]=='-')
					s[z+x]='+';
					else
					s[z+x]='-';
				}
				cnt++;
			}
		}
		cout<<"Case #"<<y<<": ";
		if(flag==1) 
		cout<<"IMPOSSIBLE\n";
		else 
		cout<<cnt<<'\n';
	}
	return 0;
}
