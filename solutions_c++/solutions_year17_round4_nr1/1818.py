#include <iostream>
#include <fstream>
#include <iomanip>
#define DN 1000
using namespace std;

int T,fr[6],n,p,v;

int main() {
	ifstream f("a.txt");
	ofstream g("a.out");
	f>>T;
	for(int t=1; t<=T; ++t) {
		f>>n>>p;
		int r=0;
		for(int i=0; i<n; ++i) {
			f>>v;
			if(v%p==0) ++r;
			else ++fr[v%p];
		}
		for(int i=1, j=p-1; i<j; ++i,--j) {
			r+=min(fr[i],fr[j]);
			if(fr[j]>fr[i]) {
				fr[j]-=fr[i];
				fr[i]=0;
			}
			else {
				fr[i]-=fr[j];
				fr[j]=0;
			}
		}
		int ndif=0;
		for(int a=1; a<p; ++a) if(fr[a]) ++ndif;
		if(ndif==1) {
			for(int a=1; a<p; ++a) if(fr[a]) {
				for(int j=2; j<=p; ++j) if((a*j)%p==0) {
					r+=fr[a]/j;
					if(fr[a]%j) ++r;
					break;
				}
			}
		}else {
			cerr<<t<<' '<<"nasol";
		}
		g<<"Case #"<<t<<": ";
		g<<r;
		g<<'\n';

		for(int i=0; i<=p; ++i) fr[i]=0;
	}
}