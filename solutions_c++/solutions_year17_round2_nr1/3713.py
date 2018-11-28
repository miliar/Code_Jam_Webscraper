#include <iostream>
using namespace std;

int main() {
	long double n,x,i,d,h,a,b,j;
	long double z;
	cin>>n;
	for(i=1;i<=n;i++)
	{
	    cin>>d;
//	    cout<<"d"<<d<<"\n";
	    cin>>h;
//	    cout<<"h"<<h<<"\n";
	    x=0;
	    for(j=0;j<h;j++)
	    {
	        cin>>a;
//	        cout<<"a"<<a<<"\n";
	        cin>>b;
//	        cout<<"b"<<b<<"\n";
	        a=d-a;
	        b=a/b;
	        
	        x=max(b,x);
//	        cout<<"x"<<x<<"\n";
	    }
	    z=d/x;
	    cout<<"Case #"<<i<<": ";
		printf("%Lf \n",z);

	}
	return 0;
}
