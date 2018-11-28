#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int start,ende;

int getLongest(int b[],int n)
    {
        int length = 0, temp = 0;
        int len =n;
        for(int i = 1; i < len ; i++)
        {
            if (b[i] == 0)
            {
                temp++;
            }
            else{
                temp = 0;
            }
            if (length < temp)
                {	
                	length = temp;
                	ende=i+1;
                	start=ende-length-1;
                }
                
        }
        return length;
    }

int main() {
	int t,r=1,n,k;
	cin>>t;
	while(r<=t)
	{
		cin>>n>>k;
		n=n+2;
		int arr[n+1],middle;
		memset(arr,0,sizeof(arr));
		arr[1]=1,arr[n]=1;
	
	    while(k--)
	    {
			getLongest(arr,n+1);
		//	cout<<start<<ende<<endl;
			middle = (ende+start)/2;
		//	cout<<middle<<endl;
	     	arr[middle]=1;
	    }
	    
	  //  cout<<middle<<endl;
	    int li=0,ri=0;
	    
	    for(int i=middle-1;i>0;i--)
	    {
	    	if(arr[i] == 0)
	    	li++;
	    	else
	    	break;
	    }
	    
	    for(int i=middle+1;i<n+1;i++)
	    {
	    	if(arr[i] == 0)
	    	ri++;
	    	else
	    	break;
	    }
	    
	    
	    cout<<"Case #"<<r<<": "<<max(li,ri)<<" "<<min(li,ri)<<endl;
	    
	    
		r++;
	}
	return 0;
}