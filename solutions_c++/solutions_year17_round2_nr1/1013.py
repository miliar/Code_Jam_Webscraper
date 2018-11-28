#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cstdint>
#include <limits>
#include <iomanip>

using namespace std;

double solve(unsigned int d, vector<pair<unsigned int, unsigned int>> pos){
	double max = -1;

	for(auto i = pos.begin(); i != pos.end(); i++) {
		double x = (d - i->first) / (double)i->second;
		if(max < x || max < 0) {
			max = x;
		}
	}

	return d / max;
}

int main() {
	int t;
	unsigned int d, n;

	cin >> t;

	cout << setprecision(numeric_limits<double>::digits10 + 1);

	for(int i = 0; i < t; i++){
		cin >> d >> n;
		vector<pair<unsigned int, unsigned int>> pos;
		for(int j = 0; j < n; j++) {
			unsigned int k, s;
			cin >> k >> s;
			pos.push_back(make_pair(k, s));
		}
		
		cout << "Case #" << (i + 1) << ": " << solve(d, pos) << endl;
	}

	return EXIT_SUCCESS;
}
