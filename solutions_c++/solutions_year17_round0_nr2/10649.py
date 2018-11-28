#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long int val,r1,r2,n,i,j;
	int t,found;
	cin>>t;
	for(i=1;i<=t;i++)
	{
	    cin>>val;
	    found=0;
	    for(j=val;j>=1;j--)
	    {
	        n=j;
	        while(n!=0)
	        {
	            r1=n%10;
	            n=n/10;
	             if(n==0)
	               { 
	                 found=1; break;
	               }
	            r2=n%10;
	            if(r1>=r2)
	             continue;
	            break;
	        }
	        if(found==1)
	         { cout<<"Case #"<<i<<": "<<j<<"\n"; break; }
	    }
	}
	return 0;
}