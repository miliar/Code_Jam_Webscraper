#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
	long int t,k,n,c=0,i,j,m=0,z=1;
	char s[1000];
	cin>>t;
	
	while(t!=0)
	{   
	    c=0;
	    cin>>s>>k;
	    n=strlen(s);
	    m=0;
	    for(i=0;i<n;i++)
			if(s[i]=='+')
				m=m+1;
			if(m==n)
			{	cout<<"Case #"<<z<<":"<<" "<<c<<endl;
				goto l;
			}


		for(i=0;i<n;i++)
		{
			if(s[i]=='-')
			{
			    if((i+k)>n)
			        break;
				for(j=0;j<k;j++)
				{   
					if(s[i+j]=='+')
						s[i+j]='-';
					else
						s[i+j]='+';

				}
				c=c+1;
			}
			if(s[n-i-1]=='-')
			{
			    if((n-i-1-k)<0)
			        break;
				for(j=0;j<k;j++)
				{
					if(s[n-i-j-1]=='+')
						s[n-i-j-1]='-';
					else
						s[n-i-j-1]='+';


				}
				c=c+1;

			}

		}
		m=0;
		for(i=0;i<n;i++)
			if(s[i]=='+')
				m=m+1;
			if(m==n)
			{	cout<<"Case #"<<z<<":"<<" "<<c<<endl;

			}
			else
				cout<<"Case #"<<z<<":"<<" "<<"IMPOSSIBLE"<<endl;
	l:	t=t-1;
		z=z+1;

	}
	
}