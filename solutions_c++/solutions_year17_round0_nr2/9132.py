#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long long int t,i,j,k,z,x,m=0,r;
	char s[10000];
        cin>>t;
	while(t--)
	{
		m++;
		x=0;
		cin>>s;
		k=s[0]-'0';
		x=0;
		r=0;
		for(i=1;i<strlen(s);i++)
		{

			j=s[i]-'0';
			if(j>k)
			{
				x++;
			}
			else if(k>j)
			{
				r=1;
				break;
			}
			k=j;
			//cout<<s[i]<<endl;
		}
		if(r==0)
		{
			cout<<"Case #"<<m<<": "<<s<<endl;
			continue;
		}
		k=s[x]-'0';
		k--;
		s[x]=k+'0';
		for(i=x+1;i<strlen(s);i++)
		{
			s[i]='9';
		}

		cout<<"Case #"<<m<<": ";
		k=0;
		for(i=0;i<strlen(s);i++)
		{
			if(s[i]=='0' && k==0)
			{
				continue;
			}
			else
			{
				cout<<s[i];
				k++;
			}
		}
		cout<<endl;		
	}
	return 0;
}