#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace std;
long long max1(long long x,long long y)
{
	if(x>y)
		return x;
	else
		return y;
}
long long int div(long long first,long long last,long long k)
{

	long long x,y,mid;
	if(first>last)
		return 0;
	if(k==0)
	{
		return last-first+1;
	}
	mid=(first+last)/2;

	if(k==1)
		return last-mid;

	
	if(k%2==0)
		return div(mid+1,last,k/2);
	else
		return div(first,mid-1,(k-1)/2);

}
long long int divv(long long first,long long last,long long k)
{

	long long x,y,mid;
	if(first>last)
		return 0;
	if(k==0)
	{
		return last-first+1;
	}
	mid=(first+last)/2;

	if(k==1)
		return mid-first;

	if(k%2==0)
		return divv(mid+1,last,k/2);
		
	else
		return divv(first,mid-1,(k-1)/2);

}
int main()
{
	long long int N,k,x,y;
	//long long n,n1,out;
	int T,c;
	//char str[100]; 
	//char temp;
	cin>>T;
	c=1;
	while(T--)
	{
		cin>>N;
		cin>>k;
		x=div(0,N-1,k);
		y=divv(0,N-1,k);
		
		cout<<"Case #"<<c<<": "<<x<<" "<<y<<endl;
		c++;
		
	}
	return 0;
}