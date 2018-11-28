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
		cin>>str;
		int i,j,l,c=0;
		l=str.length();
		for(i=0;i<l-1;i++)
		{
			if(str[i]>str[i+1])
			{
				for(j=i+1;j<l;j++)
					str[j]='9';
				str[i]=str[i]-1;
				for(j=i;j>0;j--)
				{
					if(str[j]<str[j-1])
					{
						str[j]='9';
						str[j-1]=str[j-1]-1;


					}
					else
						break;
				}

			}
		}
		string str2;
		if(str[0]=='0')
		{
			cout<<"Case #"<<k<<": ";
			for(i=1;i<l;i++)
				cout<<str[i];
			cout<<endl;
		}
		else
			cout<<"Case #"<<k<<": "<<str<<endl;
		
		
		
		
	}
}