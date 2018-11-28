#include<fstream>
#include <iostream>
#include<string.h>
#include<fstream>
#include<stdlib.h>
using namespace std;
int length(int i)
{
	int k=0;
	int l=10;
	while(i!=0)
	{
		i=i/10;
		k++;
	}
	return k;
}
int main()
{
    int m=1;
	freopen("B-small-attempt1.in","r",stdin);
    freopen("submit.out","w",stdout);
	int n;
	cin>>n;
	while(n--)
	{
		int k;
		cin>>k;
		int l=length(k);
		//cout<<"l is"<<l<<endl;
		int *arr=new int[l];
		int index=l-1;
		while(k!=0)
		{
			arr[index]=k%10;
			k=k/10;
			index--;

		}
		int flag=0;
		for(int i=0;i<l-1 && i>=0;i++)
		{
			if(arr[i]>arr[i+1])
			{
				arr[i]=arr[i]-1;
				int next=i+1;
				while(next<l)
				{
					arr[next]=9;
					next++;
				}
				i=i-2;
			}

		}
		k=0;
		int k1=1;
		for(int i=0;i<l;i++)
		{
			k=k+arr[l-1-i]*k1;
			k1=k1*10;
		}
		cout<<"Case #"<<m<<": "<<k<<"\n";
		m++;
	}
	return 0;
}
