#include <iostream>
#include<vector>
using namespace std;
#define ll long long int

int main() {
	int t;
	cin>>t;
	cout <<fixed;
	cout.precision(6);
	int r=0;
	while(t>0)
	{
		r++;
		t--;
	ll dist,n;
	cin>>dist>>n;
	vector<ll> st(n);
	vector<double> sp(n);
	for(ll i=0;i<n;i++)
	cin>>st[i]>>sp[i];
	double d;
	d=(dist-st[0])/sp[0];
	for(ll i=1;i<n;i++)
	{
		//if((double)(dist-st[i])/(double)sp[i]>d)
		d=max(d,(dist-st[i])/sp[i]);
	}
	double ans=dist/d;

	cout <<"Case #"<<r<<": "<<ans<<endl;  
	
	}

	return 0;
}