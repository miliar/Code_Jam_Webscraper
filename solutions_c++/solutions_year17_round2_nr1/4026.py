#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main() {
    ll test;
    cin>>test;
    for(ll z=1;z<=test;z++)
    {
    double s,k,h,p,max=0,p1;
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
cout<<"Case #"<<z<<": "<<p1<<std::endl;

    }
	
	return 0;
}