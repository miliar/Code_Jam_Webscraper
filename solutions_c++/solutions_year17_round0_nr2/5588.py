#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	long long int t;
	
	cin>>t;
	
    for(int c=1;c<=t;c++)
	{
	    long long int n;
	    
	    cin>>n;
	    long long int temp=n;
	    long long int i=0,a[30],b[30];
	    
    	    while(temp)
    	    {
    	        a[i]=temp%10;
    	        temp/=10;
    	        ++i;  
    	    }
    	    long long int x=i;
    	    for(int j=0;j<i;j++)
    	        {   x--;
    	            
    	            b[j]=a[x];
    	     
    	        }
    	  for(int j=i-1;j>=0;j--)
    	    {   
    	        if(b[j]<b[j-1])
    	        {
    	            b[j]=9;
    	            b[j-1]=b[j-1]-1;
    	        
    	        }
    	          
    	    }
    	     for(int j=0;j<i;j++)
    	        {
    	            if(b[j]>b[j+1])
    	        {
    	            b[j+1]=9;
    	        
    	        }
    	        }
    	  cout<<"case #"<<c<<": ";
    	    for(int j=0;j<i;j++)
    	        {   if(j==0&&b[j]==0)
    	                { }
    	            else
    	            cout<<b[j];
    	     
    	        }
 
    	  cout<<endl;
	    
	}
	return 0;
}