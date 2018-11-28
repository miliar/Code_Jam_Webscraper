#include <iostream>
#include<string.h>
#include<fstream>
#include<stdlib.h>
using namespace std;
int main()
{
	freopen("B-small-attempt1 (2).in","r",stdin);
    freopen("submit.out","w",stdout);
	int test;
	cin>>test;
	for(int j=1;j<=test;j++)
	{

		int k;
		cin>>k;
		int l;

		int k1=0;
		int l1=10;
		int i=k;
		while(i!=0)
		{
			i=i/10;
			k1++;
		}
		l=k1;
		int number[1000];
		int d=l-1;
		while(k!=0)
		{
			number[d]=k%10;
			k=k/10;
			d--;

		}
		for(int i=0; i>=0 && i<l-1;i++)
		{
			if(number[i]>number[i+1])
			{
				number[i]=number[i]-1;
				int n1=i+1;



				while(n1<l)
				{
					number[n1]=9;
					n1++;
				}
				i=i-2;
			}

		}
		k=0;
		int ones=1;
		for(int i=0;i<l;i++)
		{
			k=k+number[l-1-i]*ones;
			ones=ones*10;
		}
		cout<<"Case #"<<j<<": "<<k<<"\n";
	}
	return 0;
}
