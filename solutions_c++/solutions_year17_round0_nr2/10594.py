#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		long long n;
		cin>>n;
		int a[100],cnt=0,flg=0,aflg=0;
		while(n>0)
		{
			a[cnt++]=n%10;
			n/=10;
		}
		for(int i=cnt-1; i-1>=0 && i>=0;i--)
		{
			if(a[i]>a[i-1] && flg==0)
			{
				a[i]=a[i]-1;
				a[i-1]=9;
				flg=1;
			}
			if(flg==1)
			{
				a[i-1]=9;
			}
		}
		int j=0;
		while(j<100)
		{
		    flg=0;
		for(int i=cnt-1; i-1>=0 && i>=0;i--)
		{
			if(a[i]>a[i-1] && flg==0)
			{
				a[i]=a[i]-1;
				a[i-1]=9;
				flg=1;
			}
			if(flg==1)
			{
				a[i-1]=9;
			}
		}
		j++;
		}
		cout<<"Case #"<<z<<": ";
		for(int i=cnt-1;i>=0;i--)
		{
		    if(a[i]!=0)
		    {
		        aflg=1;
		    }
		    if(aflg==1)
		        cout<<a[i];
		}
		cout<<endl;
	}
}
