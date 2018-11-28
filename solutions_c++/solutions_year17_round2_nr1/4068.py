#include <bits/stdc++.h>
using namespace std;

int main() {
	int r;
	cin>>r;
	for(int y=1;y<=r;y++)
	{
		long long d;
		int n;
		cin>>d>>n;
		long long ds[n],s[n];double nam[n];
		
		
		for(int i=0;i<n;i++)
		cin>>ds[i]>>s[i];
		for(int i=0;i<n;i++)
		
		
		nam[i]=(double)((double)(d-ds[i])/(double)s[i]);
		
		
		sort(nam,nam+n);
		
		
		cout<<"Case #"<<y<<": "<<fixed<<setprecision(6)<<(double)(d/nam[n-1])<<endl;
	}
	return 0;
}