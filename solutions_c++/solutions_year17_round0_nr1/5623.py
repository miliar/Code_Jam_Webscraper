#include<iostream>
#include<string.h>
using namespace std;
int main()
{   freopen("A-large.in","r",stdin);
    freopen("out140.txt","w",stdout);
	int t,x=1,k,p,i,j,r,s;
	char ch[1000];
	cin>>t;
	while(t--)
	{
		cin>>ch;
		cin>>k;
		p=strlen(ch);
		i=0;
		r=0;
		s=0;
		while(i<p-k+1)
		{
			if(ch[i]=='+')
			i++;
			else
			{
				r++;
				for(j=0;j<k;j++)
				if(ch[i+j]=='+')
				ch[i+j]='-';
				else
				ch[i+j]='+';
			}
		}
		for(;i<p;i++)
		if(ch[i]=='-')
		{
			s=1;
			break;
		}
		if(s==0)
		cout<<"Case #"<<x<<": "<<r<<endl;
		else
		cout<<"Case #"<<x<<": "<<"IMPOSSIBLE"<<endl;
		x++;
	}
	return 0;
}
