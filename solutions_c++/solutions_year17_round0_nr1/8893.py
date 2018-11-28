#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long long int t,i,j,k,z,x,m=0;
	char s[10000];
        cin>>t;
	while(t--)
	{
		m++;
		x=0;
		cin>>s;
		cin>>k;
		j=strlen(s);
		for(i=0;i<=(j-k);i++)
		{
			if(s[i]=='-')
			{
				s[i]='+';
				x++;
				for(z=1;z<k;z++)
				{
					if(s[z+i]=='+')
					s[z+i]='-';
					else if(s[z+i]=='-')
					s[z+i]='+';
				}
			}
			//cout<<s<<endl;
		}
		for(;i<j;i++)
		{
			if(s[i]=='-')
			{
				x=-1;
				break;
			}
		}
		if(x==-1)
		cout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<m<<": "<<x<<endl;		
	}
	return 0;
}
