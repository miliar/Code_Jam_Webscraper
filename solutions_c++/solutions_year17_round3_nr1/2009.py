#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <map>
#include <vector>
#include <iomanip>      // std::setprecision
#include <algorithm>

#define _USE_MATH_DEFINES
# define M_PI           3.14159265358979323846  /* pi */
using namespace std;  // since cin and cout are both in namespace std, this saves some text
long double GE(int r, int h) {
	return (long long)(((long long)r * (long long)r) * (long long)M_PI) + ((long long)2 + (long long)M_PI * (long long)r * (long long)h);
}
long double GH(int r, int h) {
	return (long double)((long double)M_PI * (long double)2 * (long double)r * (long double)h);
}
long double GS(int r) {
	return (long double)((long double)M_PI * (long double)(r) * (long double)(r));
}

long double GA(int *rop, int *hop, int nos, int cos, int nop,int cr, int cj, long double ce) {
	if (cos >= nos) {
		return ce;
	}
	else {
		if (cj >= nop) {
			return 0;
		}
		else {
			// plus j,
			long double ce1 = ce;
			long double ce2 = ce;
			if (rop[cj] > cr) {
				ce1 += GS(rop[cj]) - GS(cr);
			}
			ce1 += GH(rop[cj], hop[cj]);
			ce1 = GA(rop, hop, nos, cos + 1, nop, max(cr, rop[cj]), cj + 1, ce1);

			// plus next j
			ce2 = GA(rop, hop, nos, cos, nop, cr, cj + 1, ce2);
			if (ce2 > ce1)
				return ce2;
			else
				return ce1;
		}
	}
}

void main() {
	int t, a;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		int nop, nos;
		int rop[1001], hop[1001];
		//vector<int> radius;
		//vector< vector<int> > rtp;

		//for (int k = 0; k < 1001; k++) {
		//	rtp.push_back(vector<int>()); // Add an empty row
		//}
		setprecision(6);
		cin >> nop >> nos;
		for (int j = 0; j < nop; j++) {
			cin >> rop[j] >> hop[j];
			//if (find(radius.begin(), radius.end(), rop[j]) != radius.end()) {
			//	radius.push_back(rop[j]);
			//}
			//rtp[rop[j]].push_back(j);
		}

		std::cout << std::fixed;
		std::cout << std::setprecision(6);
		cout << "Case #" << i << ": " << GA(rop, hop, nos, 0, nop, 0, 0, 0.0) << endl;

	}
}