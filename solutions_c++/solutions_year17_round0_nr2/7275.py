#include <iostream>
#include <cmath>
using namespace std;

int main() {
	long long t,n,x,i,l,current,d,p,prev,start,end,ans;
	int flag;
	cin>>t;
	
	for(p=1;p<=t;p++)
	{
	    cin>>n;
	    l = 0;
	    flag = 1;
	    
	    x = n;
	    while(x>0)
	    {
	        l += 1;
	        x = x/10;    
	    }
	    
	    int a[l];
	    ans = 0;
	    x = n;
	    i = l-1;
	    while(x>0)
	    {
	        a[i] = x%10;
	        i--;
	        x = x/10;
	    }
	    start = 0;
	    end = 0;
	    
	    for(i=0;i<l-1;i++)
	    {
	        if(a[i]>a[i+1])
	        {
	            flag = 0;
	            break;
	        }
	        else if(a[i]!=a[i+1])
	        {
	            start = i+1;
	            end = i+1;
	        }
	        else
	        {
	            end += 1;
	        }
	    }
	    
	    if(flag==0)
	        {
        	    a[start] -= 1;
        	    
        	    for(i=start+1;i<l;i++)
        	    {
        	        a[i] = 9;
        	    }
        	    
	        }
	        
    	    for(i=l-1;i>=0;i--)
    	    {
    	        ans += a[i]*pow(10,(l-i-1));
    	    }
    	    cout<<"Case #"<<p<<": "<<ans<<endl;
	}
	return 0;
}
