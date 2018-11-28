#include<iostream>
using namespace std;

int main()
{ 
	int t,i,res[101],rem,rem1;
	unsigned long long int n,j,m,last;
	
	cin>>t;
	
	for(i=0;i<t;i++)
	{
		cin>>n;
		for(j=n+1;j>=1;)
		{
			label:
				j--;
			if(j%10!=0)
			{
				m=j;
				rem=m%10;
				m=m/10;
				
				while(m)
				{
					rem1=m%10;
					if(rem1>rem)
						goto label;
					rem=rem1;
					m=m/10;	
				}
				last=j;
				break;	
			}
		}
		res[i]=last;
	}
	
	for(i=0;i<t;i++)
		cout<<"case #"<<i+1<<": "<<res[i]<<endl;
	
	return 0;
}
