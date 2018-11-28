#include <algorithm>
#include <iostream>
using namespace std;
int main(void) {
	int test=1,t;
	cin>>t;
	while(test<=t)
	{int n,k,a[1000];
    	cin>>n;
    	cin>>k;
    	int p=0,l=1,i=0;
    	a[i]=n;
    	 int count=0; 
    	while(1)
    	{ sort(a,a+count+1);
    	    p++;
    	    if(a[i]%2==0)
    	    {
        	    a[i]=(a[i]-1)/2;
        	    a[i+1]=a[i]+1;
        	   if(p==k)  
        	    {
        	        cout<<"case #"<<test<<": "<<max(a[i],a[i+1])<<" "<<min(a[i],a[i+1])<<endl;
        	       
        	        goto ravi;
        	        
        	    }
                i++;count++;
        	    
        	}
    	    else
    	    {   
        	    a[i]=a[i]/2;
        	    a[i+1]=a[i];
        	    if(p==k)  
        	    {
        	        cout<<"case #"<<test<<": "<<max(a[i],a[i+1])<<" "<<min(a[i],a[i+1])<<endl;
        	        count++;
        	        goto ravi;
        	        
        	    }
        	    i++;count++;
        	}
    	    
    	}
    ravi:
    
    test++;
    }
	return 0;
}

