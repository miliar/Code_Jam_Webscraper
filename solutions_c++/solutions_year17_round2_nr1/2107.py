#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	long t, n;
	
	double d, k,s,m=0;
	cin>>t;
	for (long ti = 1; ti <= t; ++ti) {
		cout<<"Case #"<<ti<<": ";
		cin>>d>>n;
		m=0;
		for (long i = 0; i < n; ++i) {
			cin>>k>>s;
			float x = (d-k)/s;
			if (x > m) m = x;
		}
		
		printf("%.7lf\n", d/m);
//		cout<<d/m<<"\n";
	}
}

