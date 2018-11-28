#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		long long d;
		int n;
		cin>>d>>n;
		long long dd[n],s[n];double man[n];
		for(int j=0;j<n;j++)
		cin>>dd[j]>>s[j];
		for(int j=0;j<n;j++)
		man[j]=(double)(((double)d-dd[j])/(double)s[j]);
		sort(man,man+n);
		cout<<"Case #"<<i<<": "<<fixed<<setprecision(10)<<(double)(d/man[n-1])<<endl;
	}
	return 0;
}