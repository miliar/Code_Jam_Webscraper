#include<iostream>
#include <string.h>
using namespace std;
main()
{
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		string str;
		int p;
		cin>>str;
		cin>>p;
		int i,j,q,l,c=0,f=0;
		l=str.length();
		for(i=0;i<=l-p;i++)
		{
			 if(str[i]=='-')
			 {
			 	c++;
			 	for(j=0;j<p;j++)
			 	{
			 		//cout<<str[i+j]<<" "<<i+j <<" ";
			 		if(str[i+j]=='-')
			 			str[i+j]='0';
			 		else
			 			str[i+j]='-';
			 	}
			 	
			 }
			 //cout<<str<<endl;
		}
		f=0;
		for(j=0;j<l;j++)
		{
			if(str[j]=='-')
			{
				f=1;
				break;
			}
		}
		//cout<<str<<endl;
		if(f==0) 
			cout<<"Case #"<<k<<": "<<c<<endl;
		else
			cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
		
	}
}