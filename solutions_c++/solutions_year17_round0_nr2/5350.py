#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>>T;
	while(T)
	{
	    long long int n,no;
	    int m,len,flag=0;
	    len=0;
	    cin>>n;
	    no=n;
	    while(no>0)
	    {
	       no=no/10; 
	       len++;
	    }
	    no=n;
	    int a[len];
	    for(int i=len; i>0;i--)
	    {
	           
	           a[i-1]=no%10;
	           no=no/10;
	          
	    }
	    int it=100;
	    while(1)
	    {
	        for(int i=0;i<len-1;i++)
	        {
	            if(a[i]>a[i+1])
	            {
	                a[i]--;
	                for(int j=i+1; j<len;j++)
	                {
	                    a[j]=9;
	                }
	                break;
	            }   
	            
	        }
	       
	        for(int i=0;i<len-1;i++)
	        {
	            if(a[i]>a[i+1])
	            {
	                flag=1;
	                break;
	            }
	        }
	        if(flag==0)
	        {
	            break;
	        }
	        else
	        {
	            flag=0;
	            //continue;
	        }
	        
	        
	    }
	    if(a[0]==0)
	        {
	            m=1;
	        }
	        else
	        {
	            m=0;
	        }
	    for(m;m<len;m++)
	    {
	        
	        
	        cout<<a[m];
	    }
	    cout<<"\n";
	    T--;
	}
	
	
	return 0;
}
