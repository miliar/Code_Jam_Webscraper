#include<iostream>

using namespace std;

int test_tidy(int n)
{
	int a[20],rem, i=0,j, flag=0;
	if(n<10)
		return 1;
	else
	{	
		while(n!=0)
		{
			a[i]=n%10;
			n=n/10;
			i++;
		}
		for(j=0; j<i-1 && flag==0; j++)
		{
			if(a[j]<a[j+1])
				flag=1;
		}
		if(flag==0)
			return 1;
		else 
			return 0;	
	}
}


int main()
{
	int n;
	cin>>n;
	int a, flag,j,i;
	for(i=1; i<=n; i++)
	{
		cin>>a;
		flag=0;
		for( j=a; j>=0 && flag==0; j--)
		{
			
			if(test_tidy(j)==1)
			{
				cout<<"Case #"<<i<<": "<<j<<"\n";
				flag=1;
			}
		}
	}
	return 0;
}
