#include<bits/stdc++.h>
typedef long long int lli;
using namespace std;
int main()
{
	lli t,a,b,c,d=0;
	string s;
	cin>>t;
	while(t--)
	{   b=19;
	    
		cin>>s;
		a=s.length();
		d++;
		if(a==1)
		{
			//do nothing
		}
		else
		{
		for(int i=0;i<a-1;i++)
		{
			if(s[i]>s[i+1])
			{
			  b=i;	
			  break;
			}
		}
		if(b!=19)
		
		{
		
		for(int i=0;i<a;i++)
		{
           if(s[i]==s[b])
           {
           	c=i;
           	break;
		   }
		}
		for(int i=c+1;i<a;i++)
		{
			s[i]='9';
		}
		s[c]=s[c]-1;
								
		}
	}
		cout<<"Case #"<<d<<": ";
		if(s[c]=='0')
		{
			for(int i=1;i<a;i++)
			cout<<s[i];
					}
		else
		{
			for(int i=0;i<a;i++)
			cout<<s[i];			
				}
				cout<<"\n";		
	}
	return 0;
}
