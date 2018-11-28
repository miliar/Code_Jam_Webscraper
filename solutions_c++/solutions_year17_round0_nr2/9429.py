#include <iostream>
#include <cstdio>
#include <string.h>
#include <math.h>
#define p printf
#define loop(i,n) for(int i=0;i<n;i++)
using namespace std;

int main()
{
	int t;
	cin>>t;
	long long n;
	long long int arr[100];
	int c=0;
	for(int k=1;k<=t;k++)
	{
		cin>>n;
		int flag=1;
		long long a=n;
		int prev=9;
		c=0;
		while(a)
		{
			int d=a%10;
			arr[c++]=d;
			if(d>prev)
			{
				flag=0;
			}
			a/=10;
			prev=d;
		}
		arr[c]=0;
		c++;
		if(flag==1)
		{
			cout<<"Case #"<<k<<": "<<n<<"\n";
		}
		else
		{
			int idx=0,f=1;
			for(int m=c-2;m>0;m--)
			{
				
				if(arr[m]>=arr[m-1])
				{
					f=0;
					idx=m;
					break;
				}

			}
			if(f!=0)
			{
				idx=c-2;
			}
			long long ans=0;
			ans+=arr[idx]*pow(10,idx);
			ans--;
			if(arr[idx+1]!=0)
			{	
				for(int j=idx+1;j<c-1;j++)
				{
					ans=ans+(arr[j]*pow(10,j));
				}
			}
			cout<<"Case #"<<k<<": "<<ans<<"\n";
		}
	}
	return 0;
}
//111 111 111 111 111 110
//100 000 000 000 000 000
//999 999 999 999 999 99