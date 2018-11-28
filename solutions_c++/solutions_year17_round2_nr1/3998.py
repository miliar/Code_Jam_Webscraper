#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main() {
    ll t,z;
    cin>>t;
    for(z=0;z<t;z++)
    {
    float s,k,h,p,max=0,p1;
    ll n,d,i;
    cin>>d>>n;
    
    for(i=0;i<n;i++)
    {cin>>k>>s;
    p=d-k;
    h=(d-k)/s;
    if(h>max)
    max=h;
        
    }
     p1=d/max;
   cout<<std::fixed;
    cout<<std::setprecision(6);
cout<<p1<<std::endl;
cout.flush();
    }
	// your code goes here
	return 0;
}
