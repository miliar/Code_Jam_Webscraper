#include<iostream>

using namespace std;

int main()
{
	int testCases,i;
	cin>>testCases;
	for(i=1;i<=testCases;i++)
	{
		long long int n,j;
		cin>>n;
		long long tmp=n;
		string ss =to_string(n);
		int size_ = ss.length();
		int arr[size_];
		for(j=size_-1;j>=0;j--)
		{
			arr[j]=tmp%10;
			tmp=tmp/10;
		}

		for(j=size_-1;j>0;j--)
		{
			if(arr[j]<arr[j-1])
			{
				for(int k=j;k<size_;k++)
				{
					if(arr[k]!=9)
					arr[k]=9;
				}
				arr[j-1]--;
			}
		}
		j=0;
		if(arr[j]==0)
		j++;
		cout<<"Case #"<<i<<": ";
		for(;j<size_;j++)
		{
			cout<<arr[j];
		}
		cout<<endl;
	}
}
