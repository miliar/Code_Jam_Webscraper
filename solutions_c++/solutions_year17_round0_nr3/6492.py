//============================================================================
// Name        : codejam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

 int main() {

	freopen("C-small-1-attempt3.in.txt","r", stdin);
	freopen("output.txt","w", stdout);
	long long int t;
	cin>>t;
	long long int zz=1;
	while(t--)
	{
		long long int n,k;
		cin>>n>>k;
		long long int stall[n+2];
		for(long long int i=1;i<=n;i++)
		{
			stall[i]=0;
		}
		stall[0]=1;
		stall[n+1]=1;
		long long int fmin=1,fmax=n;
		long long int count1=0,count2=0;
		//long long int longest=max-min+1;
		for(long long int i=1;i<=k;i++)
		{
			long long int x=(fmax+fmin)/2;
			//cout<<"MARKING on : ";
			//cout<<x<<endl;
			stall[x]=1;


			long long int longest=0;
			long long int min=0,max=0,q=0;
			fmax=0,fmin=0;


			for(long long int j=1;j<=n;)
			{

				if(stall[j]==0)
				{
					min=j;
					//cout<<"MIN : "<<min<<endl;
					for(long long int z=j;z<=n+1;z++)
					{
						if(stall[z]==1)
							{
							max=z-1;
							///cout<<"MAX : "<<max<<endl;
							break;
							}
					}
					q=max-min+1;

				 if(q>longest)
				 	{
					fmax=max;

					fmin=min;
					//cout<<fmin<<endl;
					//cout<<fmax<<endl;
					longest=q;
					//cout<<"LONGEST : "<<q<<endl;

				}
				}
				else
				{
					j++;
					continue;
				}
				j++;
				//j=j+longest+1;

			}

			if(i==k)
			{
				for(long long int i=x+1;i<=n;i++)
				{
					if(stall[i]==0)
						count1++;
					if(stall[i]==1)
						break;
				}
				for(long long int i=x-1;i>=1;i--)
				{
					if(stall[i]==0)
						count2++;
					if(stall[i]==1)
						break;
				}
			}
		}
		cout<<"Case #"<<zz<<": "<<max(count1,count2)<<" ";
		cout<<min(count1,count2)<<endl;
		zz++;


		//for(long long int i=1;i<=n;i++)
		//	cout<<stall[i]<<" ";



	}
	return 0;
}
