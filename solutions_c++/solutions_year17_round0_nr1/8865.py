#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;

bool check(string s1)
{
	long int count=0;
	long int l=s1.length();
	for(long int i=0; i<l; i++)
	{
		if(s1[i] == '+')
			count++;
	}
	if(count==l)
		return true;
	else
		return false;
}

int main()
{
	long int T,k,len,loc,count=0,*c;
	string s;
	cin>>T;

	c=new long int[T];

	for(long int k1=0; k1<T; k1++)
	{count=0;
	cin>>s>>k;
	len=s.length();
	for(long int i=0; i<(len-k+1); i++)
	{
		loc=i;
		if(s[i] == '-')
		{
			for(long int  j=loc; j<(loc+k); j++)
			{
				if(s[j] == '-')
					s[j] = '+';
				else if(s[j] == '+')
					s[j] = '-';
			}
			//cout<<s<<endl;
			count++;
		}
	}
	bool ans=check(s);
	if(ans)
		c[k1]=count;
	else
		c[k1]=-1;
	}

	for(long int k1=0; k1<T; k1++)
	{
		if(c[k1]!=-1)
			{cout<<"Case #"<<(k1+1)<<": ";
			cout<<c[k1]<<endl;}
		else
		{cout<<"Case #"<<(k1+1)<<": ";
			cout<<"IMPOSSIBLE"<<endl;}
	}
}

