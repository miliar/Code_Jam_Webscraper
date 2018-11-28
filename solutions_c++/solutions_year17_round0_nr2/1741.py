#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace std;
int main()
{
	int T,i,p,prev,x,j,flag,first,l,c;
	long long n,n1,out;
	char str[100]; 
	char temp;
	cin>>T;
	c=1;
	while(T--)
	{
		cin>>n;
		n1=n;
		l=0;
		prev=9;
		l=0;
		while(n1)
		{
			x=n1%10;
			str[l]=x+'0';
			l++;
			n1=n1/10;
		}
		str[l]='\0';
		//printf("%s\n",str);

		for(j=0;j<l/2;j++)
		{
			temp=str[j];
			str[j]=str[l-j-1];
			str[l-j-1]=temp;
		}
		
		str[l]='\0';
		p=str[0]-'0';
		//cout<<p<<endl;
		//printf("%s\n",str);
		out=n;
		
		for(i=0;i<l-1;i++)
		{
			
			if(str[i]-'0'>str[i+1]-'0')
			{
				//cout<<i<<endl;
				//str[i]=str[i]-1;
				flag=0;
				for(j=i;j>0;j--)
				{
					if(str[j]!=str[j-1])
					{
						first=j;
						flag=1;
						break;
					}

				}
				if(flag==0)
				{
					first=0;
					if(str[first]=='1')
					{
						out=9;
						for(j=0;j<l-2;j++)
						{
							out=out*10+9;
						}
						break;
					}
				}
				//cout<<first<<endl;
				p=str[first] - '0';
				p=p-1;
				//cout<<str[first]<<endl;
				str[first]=p+'0';
				for(j=first+1;j<l;j++)
				{
					str[j]='9';
				}
				out=str[0]-'0';
				for(j=1;j<l;j++)
				{
					out=out*10+(str[j]-'0');
				}
				break;
			}
		}
		cout<<"Case #"<<c<<": "<<out<<endl;
		
		
		c++;
		
	}
	return 0;
}