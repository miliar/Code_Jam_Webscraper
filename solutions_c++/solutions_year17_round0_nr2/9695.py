#include <iostream>
using namespace std;

int main() {
	int t,s1;


	cin>>t;
	int c=1;
	while(t--)
	{
	    long long int n,res=0;
	    cin>>n;
	   long long int dig=0,max=0,sum=1;

	    if(n)
	    {
	        int c1=1;
	    int f=0;
	    max=n%10;
	    n=n/10;
	    while(n>0)
	    {

	            dig=n%10;
	            n=n/10;

	           if(max==0 || max<dig)
	           {
	               s1=9;
	               f=1;
	           }
	           else
	           {
	               s1=max;
	               f=0;
	           }

	           if(f==1 && dig!=0)
	            {
	                max=dig-1;
	            }
	           else
	           {
	               max=dig;
	           }
	           if(f==1)
	           {
	               int c2=c1;
	               res=0;
	               sum=1;
	               while(c2--)
	               {
	           res=sum*s1+res;
	           sum=sum*10;
	               }
	           }
	           else
	           {
	               res=sum*s1+res;
	           sum=sum*10;
	           }
c1++;


	    }
	    res=sum*max+res;
	    cout<<"Case #"<<c++<<": "<<res<<endl;
	    }
	    else
	    cout<<"Case #"<<c++<<": "<<0<<endl;

	}
	return 0;
}
