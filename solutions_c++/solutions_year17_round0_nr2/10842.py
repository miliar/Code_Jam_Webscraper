#include<iostream>
using namespace std;

int main()
{
	int t,n,arr[1001];
	cin>>t;
	int p=1;
	while(t--)
	{
		cin>>n;
		while(n>0)
		{
			
			int num=n;
			int i=0,temp=0,c=0;
			while(num>0)
			{
				arr[i]=num%10;
				num=num/10;
				i++;
			}
			for(int j=0;j<i-1;j++)
			{
				if(arr[j]-arr[j+1]>=0)
				{
					c++;
				}
				else
				{
					temp=1;
					break;
				}
			}
			if(temp==0)
			{
				cout<<"Case #"<<p<<": ";
				for(int j=i-1;j>=0;j--)
					cout<<arr[j];
				cout<<"\n";
				break;
			}
			else
			{
				n=n-1;
			}
		}
		p++;
	}
	return 0;	
}
