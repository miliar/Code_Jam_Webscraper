#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long long int hm,z,ct,temp,ola,m,nh;
	cin>>hm;
	nh=1;
	while(hm--)
	{
		ct=0,temp=0;
		string b;
		cin>>b;
		cin>>ola;
		long long int l=b.length();
		if (ola<=0)
		cout<<"Case #"<<nh<<": "<<"IMPOSSIBLE"<<endl;
		else
		{
		for(m=0;m<=(l-ola);m++)
		{
			if(b[m]=='-')
			{
				b[m]='+';
				for(z=m+1;z<m+ola;z++)
				{
					if(b[z]=='-')
					b[z]='+';
					else if(b[z]=='+')
					b[z]='-';
				}
				ct++;
				
				
			}
		}
		
        	for(m=0;m<l;m++)
			{
				if(b[m]=='-')
				{
					temp=1;
					break;
				}
			}
			if(temp==0)
			{
				cout<<"Case #"<<nh<<": "<<ct<<endl;
			}
			else
			cout<<"Case #"<<nh<<": "<<"IMPOSSIBLE"<<endl;
		}
		nh++;
     }
    
	
	return 0;
}
