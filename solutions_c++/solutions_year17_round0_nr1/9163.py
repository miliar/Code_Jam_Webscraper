#include <bits/stdc++.h>
using namespace std;
string change(string s,int i,int e)
{
	for(;i<=e;i++)
	{
		if(s[i]=='-')
		{
		
			s[i]='+';
		}
		else
		{
		
			s[i]='-';
		}	
	}
	return s;
}


int main()
{
int k,t;
string s;
cin>>t;
int c[t];
for(int x=0;x<t;x++)
{
cin>>s;
cin>>k;
int l=s.length();
c[x]=0;
for(int j=0;j<=l-k;j++)
{
	
	if(s[j]=='-')
	{
		s=change(s,j,j+k-1);
		c[x]++;
	}
}
 int n = count(s.begin(), s.end(), '-');
 if(n!=0)
 	c[x]= -1;
}
for(int x=0;x<t;x++)
{
	if(c[x]== -1)
	{
		cout<<"Case #"<<x+1<<": Impossible";
	}
	else
	{
		cout<<"Case #"<<x+1<<": "<<c[x];
	}
	cout<<endl;
}
return 0;




}


