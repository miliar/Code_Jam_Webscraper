#include <iostream>
using namespace std;


long long istrue(int b[],int n)
{
    int i=0;
    for(i=n;i>0;i--)
    {
        if(b[i]>b[i-1])
            return i;
    }
    return 0;
}


int main() {
	// your code goes here
	
	long long int i,n,z,t,n1,temp,flag,sum;
	int a[20],count=0;
	
	cin>>t;
	for(z=0;z<t;z++)
	{
	    for(i=0;i<20;i++)
	        a[i]=0;
	    cin>>n;
	    n1=n;i=0;count=0;
	    while(n1>0)
	    {
	        temp=n1%10;
	        count++;
	        a[i]=temp;
	        n1=n1/10;
	        i++;
	    }
	    i=0;count--;
	    flag = istrue(a,count);
	    while(flag!=0)
	    {
	         a[flag]=a[flag]-1;
	         for(i=flag-1;i>=0;i--)
	         {
	             a[i]=9;
	         }
	         flag=istrue(a,count);
	    }
	    sum=0;
	    for(i=count;i>=0;i--)
	    {
	        sum=sum*10+a[i];
	    }
	    cout<<"Case #"<<(z+1)<<": "<<sum<<"\n";  
	}
	return 0;
}


