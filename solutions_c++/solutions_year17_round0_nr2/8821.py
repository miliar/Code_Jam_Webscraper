#include<iostream>
#include<math.h>
#include<cstdlib>
using namespace std;
int main()
{
	long long int n;
	int t;
	cin>>t;
for(int i=1; i<=t; ++i)
{
	long long int res = 0,temp;
	cin>>n;
	temp = n;
	int size=0,check=0,rev = 0;
	int arr[20];
	while(temp>0)
	{
		arr[size++] = temp%10;
		temp = temp/10;
	}
	for(int j = 0; j< size-1; j++)
	{
		if(arr[j+1] > arr[j])
		{
			arr[j+1]--;
			arr[j] = 9;
			rev = 1;
		}
	}
	if(arr[size-1] == 0 && rev == 1)
	size--;
	for(int j = size-1; j > 0; j--)
	{
		if(check == 0)
		{
			if(arr[j] > arr[j-1])
			{
				arr[j-1] = 9;
				if(rev == 0)
				{
					arr[j]--;	
				}
				check = 1;
			}
		}
		else
		{
			arr[j-1] = 9;
		}
	}
	cout<<"Case #"<<i<<": ";
	for(int j = size-1; j >= 0; j--)
	{
		cout<<arr[j];
	}
	cout<<endl;
}
}


