#include<iostream>

using namespace std;

bool check(int n)
{	
	int i,j,a[100];
	i=0;
	while(n)
	{
		a[i++]=n%10;
		n=n/10;
	}
	for(j=0;j<i-1;j++)
	{
		if(a[j+1]>a[j])
		{
			return false;
		}
	}
	return true;
	
}

int main()
{
	int t,n,i,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n;
		for(n;n>0;n--)
		{
			if(check(n))
			{
				cout<<"Case #"<<j<<": "<<n<<endl;
				break;
			}
			
		}
	}
}
