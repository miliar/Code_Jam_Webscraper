#include <iostream>
using namespace std; 
typedef long long ll;
int iftidy(int a);
int tidy(int a);
int main()
{
	int k,i,a;
	cin>>k;
	for(i=1;i<=k;i++)
	{
		cin>>a;
		a=tidy(a);
		cout<<"Case #"<<i<<": "<<a<<"\n";
	}
	return 0;
}
int tidy(int a)
{
	while(a>9)
	{
		if(iftidy(a))
		break;
		else
		a=a-1;
	}
	return a;
}
int iftidy(int a)
{
	int t,d,flag=0;
	while(a!=0)
	{
		d=a%10;
		t=a/10;
		if(d>=t%10)
		flag=1;
		else
		{
		flag=0;break;
	    }
		a=t;
	}
	return flag;
}
