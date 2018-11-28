#include<iostream>
using namespace std;

int main()
{
	long long int par,t,j,k,n;
	cin>>par;
	for(k=1;k<=par;k++)
	{
	cin>>n;
	    long long int jer;
	long long int a[1000];
	for(t=n;t>=1;t--)
	{
	long long int flag=0;	int temp=0;
	long int M=t;
	while(M>=1)
	{
	jer=M%10;
	
	a[temp]=jer;
	temp++;
	
	M=M/10;
	}
	
	
	for(j=0;j<(temp-1);j++)
	{
	if(a[j]>=a[j+1])
	flag++;
	}
	
	if(flag==(temp-1))
	{
	
	cout<<"Case #"<<k<<": "<<t<<endl;
	break;
	}
	}
	}
	return 0;
}
