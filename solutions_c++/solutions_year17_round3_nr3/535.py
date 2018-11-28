#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;
int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int i=1;i<=t;i++) {
		int k,n;
		double u;
		in >> n >> k;
		in >> u;
		vector <double> p(n);
		for (int j=0;j<n;j++) in >> p[j];
		sort(p.begin(),p.end());
		p.push_back(1.);
		for (int j=0;j<n && u > 0.;j++) {
			if ((p[j+1]-p[j])*(j+1) < u) {
				u -= (p[j+1]-p[j])*(j+1);
				for (int l=0;l<=j;l++) p[l] = p[j+1];
			} else {
				double du = u/(j+1);
				u = 0.;
				for (int l=0;l<=j;l++) p[l] += du;
			}
		}
		double ans(1.);
		for (int j=0;j<n;j++) ans *= p[j];
		
		out.setf(ios::fixed);
		out.precision(6);
		out << "Case #" << i << ": " << ans << "\n";
	}
	return 0;
}

