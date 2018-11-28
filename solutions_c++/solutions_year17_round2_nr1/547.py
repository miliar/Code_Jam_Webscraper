#include <iostream>
#include <fstream>
#include <iomanip>
#define DN 1000
using namespace std;

int T,d,n;
int ip[DN],v[DN];

int ch(long double vc) {
	for(int i=0; i<n; ++i)
	  if(v[i]<vc && (ip[i]*vc)/(vc-v[i])<d) return 0;
	return 1;
}

int main() {
	ifstream f("a.txt");
	ofstream g("a.out");
	f>>T;
	for(int t=1; t<=T; ++t) {
		f>>d>>n;
		for(int i=0; i<n; ++i) f>>ip[i]>>v[i];

		long double ls=0,ld=1e20;
		for(int i=0; i<=100000; ++i) {
			long double m=(ls+ld)/2;
			if(ch(m)) ls=m;
			else ld=m;
		}

		g<<"Case #"<<t<<": ";
		g<<fixed<<setprecision(9)<<ls;
		g<<'\n';
	}
}