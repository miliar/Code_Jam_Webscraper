#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

int main() 
{
	ios::sync_with_stdio(0);
	int t,i,test;
	bool flag=true;
	long long int n,copy;
	vector< int > arr;
	cin>>t;
	for(test=1;test<=t;test++)
	{
		arr.clear();
		flag=true;
		cin>>n;
		copy=n;
		while(copy>0)
		{
			arr.push_back(copy%10);
			copy/=10;
		}
		for(i = 0;i<arr.size()-1;i++)
		{
			if(arr[i]<arr[i+1])
			{
				flag=false;break;
			}
		}
		if(flag)
		{
			cout<<"Case #"<<test<<": "<<n<<endl;
		}
		else
		{
			for(i=arr.size()-1;i>=0;i--)
			{
				if(arr[i] >= arr[i-1])
				{
					arr[i]--;
					for(i=i-1;i>=0;i--)
					{
						arr[i]=9;
					}
				}
			}
			for(i=arr.size()-1;i>=0;i--)
			{
				if(arr[i]!=0)
					break;
			}
			cout<<"Case #"<<test<<": ";
			for(;i>=0;i--)
			{
				cout<<arr[i];
			}
			cout<<endl;
		}
	}
}