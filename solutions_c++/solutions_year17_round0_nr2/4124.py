#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;
int mask[20];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long n,t,ans,x,y,k,a1;
	cin>>t;
	for (int q=1;q<=t;q++)
	{
		ans=0;
		cin>>n;
		x=n;
		k=0;
		for (int i=0;x>0;i++)
		{
			k++;
			mask[i]=x%10;
			x/=10;
		}
		y=1;
		while(y==1)
		{
			y=0;
			for (int i=1;i<k;i++)
			{
				if (mask[i]>mask[i-1])
				{
					y=1;
					mask[i]--;
					for (int j=0;j<i;j++)
						mask[j]=9;
				}
			}
		}
		for (int i=k-1;i>=0;i--)
		{
			ans=ans*10+mask[i];
		}
		cout<<"Case #"<<q<<": "<<ans<<"\n";
	}
	return 0;
}