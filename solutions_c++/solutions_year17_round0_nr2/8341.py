#include<iostream>
using namespace std;
int main()
{   
    freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
     
	int t;
	cin>>t;
	
	for(int madar=1 ; madar<=t ; madar++)
	{
	
	int k=0,arr[18];
	
	long long int temp,n;
	
	cin>>n;
	
    if(n<10)
	{
	cout<<"Case #"<<madar<<": "<<n;
	}
	
	else
	{
	temp=n;
	
		while(temp>=10)
		{
	    arr[k]=temp%10;
	    k++;
	    temp=temp/10;
		}
	    arr[k]=temp;
	
	
		for(int i=0 ; i<k ; i++)
		{
		 if(arr[i]<arr[i+1])
		 {
		 for(int z=0 ; z<=i ; z++)
		 arr[z]=9;
		 
		 arr[i+1]=arr[i+1]-1;	
		 }	
		}
		
		cout<<"Case #"<<madar<<": ";
		for(int i=k ; i>=0 ; i--)
		if(arr[i]!=0)
		cout<<arr[i];
	}
	cout<<endl;
	
	}
}
