#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	freopen("input.in","r",stdin);
	
	freopen("output.txt","w",stdout);
	int t;
	int print_num=1;
	cin>>t;
	while(t--)
	{
		
		long long unsigned int n;
		cin>>n;
		cout<<"Case #"<<print_num<<": ";
		print_num=print_num+1;
		if(n<10)
		{
			cout<<n<<endl;
			continue;
		}
		int rem;
		long long unsigned int num;
		num=n;
		int a[20]={0};
		int i=-1;
		int size;
		int temp;
		int index;
		while(num!=0)
		{
			i=i+1;
			a[i]=(num%10);
			num=num/10;
			
		}
		size=i+1;
		
		int j;
		
		for( j=i ; j>0 ; j-- )
		{
			if(a[j]>a[j-1])
			{
				temp=a[j];
				index=j;
				while(temp==a[index] && index<=i )
				{
				index=index+1;
				}
				
				index=index-1;
				a[index]=a[index]-1;
				for(j=(index-1); j>=0 ; j-- )
				a[j]=9;
				
				break;
				
				
			}
			
			
			
			
		}
		
		
		for(i=(size-1); i>=0 ; i-- )
		{
			if(i==(size-1) && a[i]==0 )
			continue;
			
			else
			cout<<a[i];
		}
		
		cout<<endl;
		
		
		
		
	}
	return 0;
}
