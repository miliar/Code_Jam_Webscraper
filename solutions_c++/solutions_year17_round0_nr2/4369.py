#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
    freopen("g.txt","w",stdout);
	int t,p=0;
	cin>>t;
	string s;
	while(t--)
	{
	  cin>>s;
	  	p++;
	   if(s.size()==1)
	   cout<<"Case #"<<p<<": "<<s[0]<<endl;
	   else
	   {
	   	   for(int i=s.size()-1;i>0;i--)
	  	{
	  	  if(s[i]<s[i-1])
	  	  {
	  	  	s[i-1]-=1;
	  	  	int j=i;
	  	  	while(j<s.size())
	  	  	{
	  	  	s[j]='9';
				j++	;
			}
	  	  	
		  }
		}
	     int k=0;
	     for(int i=0;i<s.size();i++)
	     {
	     	if(s[i]=='0')
	     	k++;
	     	else
	     	break;
		 }
		 cout<<"Case #"<<p<<": ";
         for(int i=k;i<s.size();i++)
	      cout<<s[i];
	      cout<<endl;
	   	
	   }
	  	
	
		
	}
}
