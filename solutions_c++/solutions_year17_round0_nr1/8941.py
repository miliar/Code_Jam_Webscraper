#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int t,l;
	cin>>t;
	for(l=0;l<t;l++)
	{
		char s[1001]="";
		int i=0,k=0,c=0,j=0;
		cin>>s;
		cin>>k;
		//cout<<s<<endl<<k<<endl;
		for(i=0;i<strlen(s)-k+1;i++)
		{
			if(s[i]=='-')
			{
			for(j=0;j<k;j++)
			if(s[i+j]=='-')
			s[i+j]='+';
			else if(s[i+j]=='+')
			s[i+j]='-';
			c++;
			}
		}
		for(i=0;i<strlen(s);i++)
		if(s[i]=='-')
		c=-1;
		if(c==-1)
		cout<<"Case #"<<l+1<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<l+1<<": "<<c<<endl;
	}
	return 0;
}