#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("otidy.txt","r",stdin);
    freopen("outputot.txt","w",stdout);
	int t;
	cin>>t;
	for(int q=1;q<=t;q++)
	{
		long long int n;
		cin>>n;
		int A[20];
		int i=0;
		while(n!=0)
		{
			int a=n%10;
			A[i]=a;
			n/=10;
			i++;
		}
		//cout<<i<<" ";
		for(int k=0;k<i;k++)
		{
			for(int j=i-2;j>=0;j--)
			{
				if(A[j]<A[j+1])
				{
					A[j+1]-=1;
					for(int w=j;w>=0;w--)
					{
						A[w]=9;
					}
					break;
				}
			}
		}
		int flag=0;
		cout<<"Case #"<<q<<": ";
		for(int e=i-1;e>=0;e--)
		{
			if(A[e]==0 && flag==0)
			{
				flag=1;
			}
			else
			{
				cout<<A[e];
			}
		}
		cout<<endl;
	}
}
