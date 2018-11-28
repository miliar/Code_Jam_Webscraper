#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main() {
	// your code goes here
	int t,y1,i,n,t1=0;
	double minm,d,k,s;
	cin>>t;
	while(t--)
	{
	    t1++;
	    minm=9999999999.0;
	    cout<<"Case #"<<t1<<": ";
	    cin>>d>>n;
	    for(i=0;i<n;i++)
	    {
	        cin>>k>>s;
	        if(minm>((double)(d*s/(d-k))))
	        minm=(double)(d*s/(d-k));
	    }
	    printf("%.9lf\n",minm);
	}
	return 0;
}

