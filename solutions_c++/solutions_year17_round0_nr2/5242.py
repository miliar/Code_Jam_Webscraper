#include<iostream>
#include<math.h>
#include<stdlib.h>
using namespace std;

long int power(long int a)
{
long int ret=1;
while(a!=0)
{
ret=ret*10;
a--;
}
return ret;
}
int getlength(long int t)
{
int c=0;
while(t!=0)
	{
	t=t/10;
	c++;
	}
return c;
}
int getdigit(long int a,long int len,long int pos)
{
	int i=0;
	pos=len-pos;
	a=a/power(pos);
	return a%10;
}

long int maketidy(long int org)
{
long int pos=1,len=getlength(org);
long int a=org,f=0;
while(pos<len)
{
while(getdigit(a,len,pos)>getdigit(a,len,pos+1))
	{
		long int temp=a+power(len-pos-1);
		if(temp<=org)
			{a=temp;f=1;}
		else
			{
			int d=getdigit(a,len,pos+1);
			long int pospow=power(len-pos);
			a=a-pospow;f=1;
			d=9-d;
			a+=d*(pospow/10);
			}
	}	
pos++;
if(f)
{
pos=1;
f=0;
}
}
return a;
}
int main()
{
int T;
cin>>T;
for(int k=0;k<T;k++)
{
	long int V;
	cin>>V;
	cout<<"Case #"<<k+1<<": "<<maketidy(V)<<endl;
}

return 0;
} 


