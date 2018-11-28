#include<iostream>
using namespace std;
int main()
{
	int t,i,k,l,f;
	long long unsigned int j,j1;
	cin>>t;
	long long unsigned int a[t],n[t];
	for(i=0;i<t;i++)
	{
		cin>>a[i];
	}
	for(i=0;i<t;i++)
	{
		for(j=1;j<=a[i];j++)
		{
			k=0;l=10;f=0;
			j1=j;
			while(j1!=0)
			{
				k=j1%10;
				if(k>l)
				{
					f=1;
					break;
				}
				l=k;
				j1=j1/10;
			}
			if(f==0)
				{n[i]=j;}
		}
		cout<<"Case #"<<i+1<<": "<<n[i]<<endl;
	}
	return 0;
}
