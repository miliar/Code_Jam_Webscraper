#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <stdlib.h>
#include <string>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <array>
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	int t;
	int D, N;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> D >> N;

		vector<array<int, 2>> v;
		vector<double> vv;
		for (int b = 0; b < N; b++)
		{
			double k, s;
			cin >> k >> s;
			double destToGo = D - k;
			double time = destToGo / s;
			//v.push_back({k, s });
			vv.push_back(time);
		}
		vector<double>::iterator result;
		result = max_element(begin(vv), end(vv));
		double val = vv[distance(begin(vv), result)];
		double kmh = D / (double)val;
		
		cout << fixed<< "Case #" << i << ": " << kmh << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}