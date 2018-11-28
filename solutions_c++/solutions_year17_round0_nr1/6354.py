#include<bits/stdc++.h>
using namespace std;

int t,k,c=0,ans=0,i,x,n;
string s;

int get_index(string s)
{
	int l=s.length();
	for(i=0;i<l;i++)
	{
		if(s[i]=='-')
		return i;
	}
	return -1;


}
int main()
{
	cin>>t;
	while(t--)
	{
		ans=0;
		c++;
		s="";
		cin>>s;
		cin>>k;
		cout<<"Case #"<<c<<": ";
		x=get_index(s);
		n=s.length();
		while(x!=-1 && x+k<=n)
		{
			
			for(i=x;i<x+k;i++)
			{
				if(s[i]=='+')
				s[i]='-';
				else if(s[i]=='-')
				s[i]='+';
			}
			x=get_index(s);
			ans++;
		}
		if(get_index(s)==-1)
		cout<<ans<<endl;
		else
		cout<<"IMPOSSIBLE\n";		
	}


	return 0;
}
