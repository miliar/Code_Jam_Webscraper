#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int t,i,num[20],msb=-1,j;
	unsigned long long int n,o;
	
	freopen("al.in","r",stdin);
	
	cin>>t;
	
	freopen("tidynum_output.txt","w",stdout);
	
	for(i=1;i<=t;++i)
	{
		cin>>n;
		o=n,msb=-1;
		
		while(n>0)
		{
			num[++msb]=n%10;
			n/=10;			
		}
		
	//	for(j=msb;j>=0;--j)
	//	cout<<num[j];
		for(j=1;j<=msb;++j)
		if(num[j]>num[j-1])
		{
			int k;
			
			//if(num[j]!=1)
			for(k=0;k<j;++k)
			num[k]=0;
			
			//o-=num[k]*pow(10,k);
			
			//o-=1;
			
			//subtract 1 from num array
			
			for(k=0;k<=msb;++k)
			if(num[k]>=1)
			{
				--num[k];
				break;
			}
			else
			num[k]=9;
			
			while(num[msb]==0)
			--msb;
		}			
		
		cout<<"Case #"<<i<<": ";
		
		for(j=msb;j>=0;--j)
		cout<<num[j];
		
		cout<<"\n";
	}
	
	return 0;	
}
