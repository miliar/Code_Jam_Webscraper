#include <bits/stdc++.h>

using namespace std;
#define ll unsigned long long int 

int main()
{
	int t;
	ll n[1000],tidy[1000];
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		cin>>n[i];
	}
	for (int i = 0; i < t; ++i)
	{
		ll temp=n[i];
		int num_digits=0,k=17;
		int num[18]={0}; 
		while(temp>0)
		{
			num[k]=temp%10;
			temp=temp/10;
			k--;num_digits++;
		}
		if(num_digits==1)
			tidy[i]=n[i];
		else
		{
			tidy[i]=0;
			int j=17;
			ll m=1;
			for (j = 17; j > 18-num_digits; j--)
			{
				if(num[j]==0)
				{	
					for (int p = j; p < 18; ++p)
					{
						num[p]=9;
					}
					if(num[j-1]>0)
						num[j-1]--;
				
				}
				else if(num[j]<num[j-1])
				{
					for (int p = j; p < 18; ++p)
					{
						num[p]=9;
					}
					num[j-1]--;
				}
				
			}
			for (j = 17; j >= 18-num_digits; j--)
			{
				tidy[i]+=num[j]*m;
				m*=10;
			}
		}
	}
	for (int i = 0; i < t; ++i)
	{
		cout<<"Case #"<<i+1<<": "<<tidy[i]<<endl;
	}
	return 0;
}