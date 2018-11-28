#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	long int t,n,n1;
	cin>>t;
	for (int i = 0; i < t; i++)
	{
		cin>>n;
		n1=n;
	if(n1>9)
	{
		while(1)
		{
			n=n1;
			int r=n%10,r1=0;
			n=n/10;
			while(n>0)
			{
				r1=n%10;
				n=n/10;
				if(r<r1)
				{
					n=1;
					break;
				}
				r=r1;
			}
			if(n==0)
				break;
			else
				n1--;
			
		}
	}
	cout<<"Case #"<<i+1<<": "<<n1<<endl;
	}
}