#include<iostream>
#include<cstdlib>
using namespace std;

int getLength(unsigned long int n)
{
	int i=0;
	while(n>0)
	{
		n=n/10;
		i++;
	}
	return i;
}

bool check(int arr[], int n)
{
	int i=0;
	bool flag=false;
	while(i < (n-1))
	{
		if(arr[i] > arr[i+1])
		{
			flag=true;
			break;
		}
		i++;
	}
	return flag;
}

void rotate(int arr[], int size)
{
	int i=0;
		for(i=0;i<size-1; i++)
		{
			if(arr[i] > arr[i+1])
			{	
				arr[i]=arr[i]-1;		
				for(int j=i+1; j<size; j++)
					arr[j]=9;
			}
		}
}

void getResult(int arr[], int size, int iteration)
{
	int i=0, j=0;
	bool flag=true;
	while(1)
	{
		while(check(arr, size))
			rotate(arr, size);
		
			cout<<"Case #"<<iteration<<": ";
			for(int k=0; k<size; k++)
			{	
				if(arr[k]==0 && k==0)
					continue;
				else
					cout<<arr[k];
			}
			cout<<endl;
			break;
	}
}

int main()
{
	int t, i, size, b=0;
	unsigned long int num;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>num;
		size=getLength(num);		
		int arr[size];
		for(int j=(size-1);j>=0;j--)
		{
			b=num%10;
			num=num/10;
			arr[j]=b;
		}
		getResult(arr, size, i);
	}
	return 0;
}
