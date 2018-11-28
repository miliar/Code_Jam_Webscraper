#include<bits/stdc++.h>
using namespace std;
void happy(string s,int n);
string s;
int t,k,j,cnt=0,c=0;
int main()
{
  	
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>s>>k;
	
		int n=s.find('-');
		if(n==-1)
		{
			cout<<"Case #"<<j<<": 0"<<endl;
			
		}
		else
		{
		happy(s,n);
		}
		c=0;
		//cout<<n;
		
	}
	return 0;
}
void happy(string s,int n)
{
	if((n+k)>s.length())
	{   
		cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
		
		
	}
	else
	{  
		for(int i=n;i<n+k;i++)
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
		c++;
		int x=s.find('-');
		if(x==-1)
		{
			cout<<"Case #"<<j<<": "<<c<<endl;
		}
		else
		{
			happy(s,x);
		}
		
		
	}
	
}
