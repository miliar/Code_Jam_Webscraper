#include<iostream>
#include<cstdio>
#include<math.h>
using namespace std;
int main()
{
	int T;
	cin >>T;
	unsigned long long int num;
	for(int i=0; i<T; i++)
	{
		int digits=0;
		int arr[30];
		memset(arr,-1,sizeof(int)*30);
		cin>>num;
		int bit = 0;
		unsigned long long int x=num;
		while(x!=0)
		{
			x=x/10;
			digits++;
		}
		x = num;
		//cout<<endl;
		for(int j=0; j<digits; j++)
		{
			arr[digits-1-j] = x%10;
			x=x/10;

		}


		for(int test=0; test<30;test++)
		{ 
			bit = 0;
			for(int k=0;k<digits-1;k++)
			{//cout<<"YOHG";
				if(bit==0)
				{
					if(arr[k] > arr[k+1])
					{
						arr[k] = arr[k] -1;
						bit=1;
					}
				}
				else
				{
					arr[k] = 9;
				}
			}
			if(bit==1)
				arr[digits-1] = 9;
		}	
		cout<<"Case #"<<i+1<<": ";
		if(arr[0]==0)
		{
			for(int kk =0; kk<digits-1;kk++)
			{
				cout<<9;
	
			}
		}
		else 
		{

			for(int kk =0; kk<digits;kk++)
			{
				cout<<arr[kk];
			}
		}

		
		
		cout<<endl;
	}

}
//111111111111111110
//99999999999999999
