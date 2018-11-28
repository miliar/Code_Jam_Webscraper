#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,tt,i,n;
double d,k,s,z;
cin>>tt;
cout.precision(6);
cout<<fixed;
for(t=1;t<=tt;t++)
{
cin>>d>>n;
z=0;
for(i=1;i<=n;i++)
{
cin>>k>>s;
z=max(z,(d-k)/s);
//cout<<z<<" "<<d/z<<endl;
}
cout<<"Case #"<<t<<": "<<d/z<<endl;
}
return 0;
}