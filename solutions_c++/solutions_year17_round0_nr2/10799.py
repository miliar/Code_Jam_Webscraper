#include<iostream>
using namespace std;
int f=0;
int n;
long int a[1000];
bool sort(int q)
{
	
	while(q>0)
	{
		int m=q%10;
		a[f++]=m;
		q=q/10;
	}
	for(int i=0;i<f-1;i++)
	if(a[i]<a[i+1])
	return false;
	return true;
}
int main()
{
	int z,m;
	m=1;
	cin>>z;
	while(m<=z)
	{
	cin>>n;
	f=0;
	cout<<"Case #"<<m<<": ";
	for(int i=n;i>0;i--)
	{
		if(sort(i))
		{
			for(int j=f-1;j>=0;j--)
			cout<<a[j];
			cout<<endl;
			break;
		}
		else
	{
		f=0;
		continue;
	}
	
}
m++;
}
}
