#include <iostream>
using namespace std;
int istidy(long long int n)
{
    int t1,t2;
    t1=n%10;
    while(n>0)
    {
        t2=n%10;
        n-=t2;
        n/=10;
        if(t2>t1)
        {
            return 0;
        }
        t1=t2;
    }
    return 1;
}
int main() {
	// your code goes here
	int t,T;
	cin>>T;
	for(t=0;t<T;t++)
	{
	    long long int n,i;
	    cin>>n;
	    for(i=n;i>0;i--)
	    {
	        if(istidy(i))
	        {
	            cout<<"Case #"<<t+1<<": "<<i<<endl;
	            break;
	        }
	    }
	}
	return 0;
}
