#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;
const double pi = 3.14159265358979323846264338327950288419716939937510582;
int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int i=1;i<=t;i++) {
		int k,n;
		in >> n >> k;
		vector <double> r(n),h(n);
		vector <int> f(n,0);
		double rm(0.);
		double g(0.);
		
		for (int j=0;j<n;j++) {
			in >> r[j] >> h[j];
		}
		
		while (k > 0) {
			int l(0);
			for (int j=0;j<n;j++) {
				if (f[j] < f[l]) l = j;
				else if (f[j] == 0 && r[j]*h[j]*2. + max(r[j]*r[j]-rm*rm, 0.) > r[l]*h[l]*2. + max(r[l]*r[l]-rm*rm, 0.)) {
					l = j;
				}
			}
			g += pi * (r[l] * h[l] * 2. + max(r[l] * r[l] - rm * rm, 0.));
			rm = max(rm, r[l]);
			f[l] = 1;
			k--;
		}
		
		out.setf(ios::fixed);
		out.precision(6);
		out << "Case #" << i << ": " << g << "\n";
	}
	return 0;
}

