#include <iostream>
#include <iomanip>
#define ull unsigned long long
using namespace std;
int main() {
	int t;
	cin>>t;
	for (int test=1;test<=t;test++)
	{
	    ull n,dist;
	    long double tm=0;
	    cin>>dist>>n;
	    ull S[n];
	    ull K[n];
	    for (int i=0;i<n;i++)
	    {
	        cin>>K[i]>>S[i];
	    }
	    for (int i=n-1;i>=0;i--)
	    {
	        if (i==n-1)
	            tm=(((long double)(dist-K[i]))/((long double)S[i]));
	        else
	        {
	            long double newt = (((long double)(dist-K[i]))/((long double)S[i]));
	            if (newt > tm)
	            tm=newt;
	        }
	    }
	    cout<<"Case #"<<test<<": "<<setprecision(15)<<(((long double)dist)/tm)<<endl;
	}
	return 0;
}
