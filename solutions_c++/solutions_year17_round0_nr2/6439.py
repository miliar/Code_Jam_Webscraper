#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int scatter(long int x, int a[])		//distributes number into array(in reverse)
{
	int ctr=0;
	for(int i=0; x>0; i++)
	{
		a[i]=x%10;
		x/=10;
		ctr++;
	}
	return ctr;
}
int inOrder(int a[],int len)
{
	int flag=1;
	for(int i=0;i<len-1; i++)
	{
		if(a[i]<a[i+1])
		{
			flag=0;
			break;
		}
	}
	return flag;	
}

int main()
{
	long int x;
	int a[20];
	int T;
	cin>>T;
	for(int q=1; q<=T; q++)
	{
	cin>>x;
	int len=scatter(x,a);
	/*
	for(int j=0;j<len;j++)
	{
		cout<<a[j];
	}
	cout<<inOrder(a,len);*/
	//cout<<"\n"<<len;
	while(!inOrder(a,len))
	{
		for(int i=0; i<len-1; i++)
		{
			if(a[i]<a[i+1])
			{
				a[i+1]-=1;
				for(int j=0;j<=i; j++)
				{
					a[j]=9;
				}
			}
		}	
	}
	if(a[len-1]==0)
		len--;
	cout<<"Case #"<<q<<": ";
	for(int p=len-1; p>=0; p--)
	{
		cout<<a[p];
	}
	cout<<endl;
	}
	return 0;
}
