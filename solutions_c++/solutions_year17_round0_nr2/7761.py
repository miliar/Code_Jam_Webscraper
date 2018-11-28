#include <bits/stdc++.h>

int main()
{
	long long int t,T,n,nu[20],i,j,k,sum;

	for(std::cin >> T, t = 1; t <= T; t++)
	{
		std::cin>>n;
		i=0;
		while(n>0)
		{
			nu[i] = n%10;
			i++;
			n/=10;
		}
		for(j=0;j<i-1;j++)
		{
			if(nu[j]<nu[j+1])
			{
				nu[j+1]--;
				for(k=j;k>=0;k--)
				{
					nu[k]=9;
				}
			}
		}
		sum =0;
		for(j=i-1;j>=0;j--)
		{
   			sum*=10;
   			sum+=nu[j];
		}
		std::cout<<"Case #"<<t<<": "<<sum<<"\n";
	}
}