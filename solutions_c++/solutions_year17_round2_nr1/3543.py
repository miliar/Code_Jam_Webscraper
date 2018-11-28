#include<iostream>
#include<algorithm>
#include<iomanip>
#define ll long long
using namespace std;

int main()
{
ll t;
cin>>t;
for(ll i=1;i<=t;i++)
{

ll d,n;
cin>>d>>n;
double x,y;
double time,tt=0;
for(ll j=0;j<n;j++)
{
	cin>>x>>y;
	time = (d-x)/y;
	if(time>tt)
		tt = time; 
}
cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<d/tt<<"\n";
}
return 0;
}