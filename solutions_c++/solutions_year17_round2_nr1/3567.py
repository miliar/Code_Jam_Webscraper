#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;cin>>t;
	long double d,k;double n,s,s1=0;
	for(int i=1;i<=t;i++)
	{
	    cin>>d>>n;s1=0;
	    while(n--)
	    {
	        cin>>k>>s;
	        if((double(d-k)/(double)s>(double)s1))
	        s1=double(d-k)/(double)s;
	    }
	    	cout<<fixed<<setprecision(6);
	    cout<<"Case #"<<i<<": "<<(double)d/(double)s1<<endl;
	    
	}
	return 0;
}
