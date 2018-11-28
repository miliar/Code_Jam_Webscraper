#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	long long int impa[t];
	long long int reala[t];
	long long int imp;
	long long int real;
	
	for(int i=0;i<t;i++)
	{
		cin>>impa[i];
		reala[i]=i;
	}
	 for(int i=0;i<t;i++)
	 {
	   imp = impa[i];
	real = imp;
	 	
	      int size=0;
	     while(imp>0)
	     {
		 
	    	imp = imp/10;
	    	size++;
		 }
        
	    int arr[size];
	    for(int a=size-1;a>=0;a--) 
	    {
	    	 arr[a] = real%10;
	    	real = real/10;
		}
		//to do calculation
		
		for(int k=size-1;k>0;k--)
		{
			if(arr[k-1]>arr[k])
			{
				arr[k-1]-=1;
				for(int z=k;z<size;z++)
				{
					arr[z]=9;
				}
			}
		}
		
	    if(arr[0]!=0)
		cout<<"Case #"<<i+1<<": "<<arr[0];
		else
		cout<<"Case #"<<i+1<<": ";
		for(int m=1;m<size;m++)
		{
			
			cout<<arr[m];
		}
        cout<<endl;
	 } 
}
