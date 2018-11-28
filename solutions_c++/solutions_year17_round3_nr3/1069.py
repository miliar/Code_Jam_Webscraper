#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <map>
#include <vector>
#include <iomanip>      // std::setprecision
#include <algorithm>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
					  // find min
long double getMin(long double core[], int noc, long double min) {
	long double cc = 1;
	for (int i = 0; i < noc; i++) {
		if (core[i] < cc && core[i] > min) {
			cc = core[i];
		}
	}
	return cc;
}
// find no of min
int getNoMin(long double core[], int noc, long double min) {
	int cc = 0;
	for (int i = 0; i < noc; i++) {
		if (core[i] == min) {
			cc++;
		}
	}
	return cc;
}
long double ceil(long double v, int p)
{
	v *= pow(10, p);
	v = ceil(v);
	v /= pow(10, p);
	return v;
}

void main() {
	cout << std::fixed;
	cout << std::setprecision(6);
	int t;
	long double a = 0;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		int noc, nos;

		long double suc;
		long double core[51];
		cin >> noc >> nos >> suc;
		suc = ceil(suc, 6);
		for (int j = 0; j < noc; j++) {
			cin >> core[j];
		}
		while (suc > 0) {
			long double min = getMin(core, noc, -0.1);
			int nrm = getNoMin(core, noc, min);
			long double smin = getMin(core, noc, min);
			if (min == 1 || suc < 0.00000001) {
				suc = 0;
				continue;
			}
			long double snpc = smin - min;
			if (snpc * nrm > suc) {
				snpc = suc / nrm;
			}

			for (int j = 0; j < noc; j++) {
				if (core[j] == min) {
					core[j] += snpc;
					suc -= snpc;
				}
			}
		}
		long double ts = 1;
		for (int j = 0; j < noc; j++) {
			ts *= core[j];
		}
		a = ts;
		cout << "Case #" << i << ": " << a << endl;

	}
}