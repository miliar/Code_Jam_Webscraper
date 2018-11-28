#include<iostream>
using namespace std;

int check(long long a)
{int t,np=0;
	t=a;
	int l1,l2;
	l1=t%10;
	
	for(t=t/10;t!=0;t=t/10,l1=l2)
	{
		l2=t%10;
		if(l2<=l1)
		{
		continue;
		}
		else
		{np=1;
			break;
		}
		
	}
	
	return np;
	
}
int main()
{
	int x,j;
	int np;
	cin>>x;
	for(j=1;j<=x;j++)
	{

	int a;
	cin>>a;
	np=check(a);
	if(np!=1)
	{
		cout<<"Case #"<<j<<": "<<a<<endl;
	}
	else
	{
		while(np!=0)
	{
	a=a-1;
			np=check(a);
	}
	
	cout<<"Case #"<<j<<": "<<a<<endl;	
	}
	
	
}
	return 0;
}

