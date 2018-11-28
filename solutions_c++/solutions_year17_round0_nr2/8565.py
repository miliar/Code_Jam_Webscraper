#include<iostream>
using namespace std;
int a[1000],b[1000];
long long int f=1;
long long  int e=1;
int main()
{
int w;
cin>>w;
for(int l=1;l<=w;l++)
	{
	f=1;
	e=1;
	long long int n;
	cin>>n;
	while(n>0)
	{
		a[f++]=n%10;
		n=n/10;
	}
	for(int i=f-1;i>0;i--)
	b[e++]=a[i];
	long long i;
	for(i=1;i<e-1;i++)
	{
		if(b[i]>b[i+1])
		{
			if(b[i-1]==b[i] && b[i]>b[i+1])
			{
				long long int q=i-1;
				while(b[q]==b[i])
				{
					q--;
				}
				q=q+1;
				b[q]=b[q]-1;
				q++;
				while(q<e)
				{
					b[q]=9;
					q++;
				}
				break;
			}
			else
			{
			  b[i]=b[i]-1;
			  long long  int q=i+1;
			   while(q<e)
					{
					b[q]=9;
					q++;
					}
					break;	
		}
	}
}
cout<<"Case #"<<l<<": ";
long long q=1;
if(b[1]==0)
q++;
for(;q<e;q++)s
cout<<b[q];
cout<<endl;
}
}
