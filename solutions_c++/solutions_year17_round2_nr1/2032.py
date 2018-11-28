#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include <cstdio>

using namespace std;

struct inp_t {
	int n;
	int d;

	vector <int> k;
	vector <int> s;

	void state() {
		cout << "state" << endl;

		cout << n << " " << d << endl;
		for(auto i: k) {
			cout << i << " ";
		}
		cout << endl;
		for(auto i: s) {
			cout << i << " ";
		}
		cout << endl;
	}
};

double solve(inp_t & inp) {

	std::stringstream sr;

//	inp.state();

	double max = -1;

	for(int i = 0; i < inp.s.size(); ++i) {
		double time = (inp.d - inp.k[i]+0.0)/inp.s[i];
//		cout << "*:" << inp.d - inp.k[i] << " " << time << endl;
		double answer = inp.d/time;
		if (max == -1)
			max = answer;

		if (max > answer)
			max = answer;
//		cout << "max:" << max << endl;
	}

	return max;
}

int main() {
	int n;
	cin >> n;
	string x;
	getline(cin, x);
	for (int l = 1; l <= n; ++l) {
		inp_t inp;
		getline(cin, x);
		stringstream ss(x);
		ss >> inp.d >> inp.n;
		inp.k.resize(inp.n);
		inp.s.resize(inp.n);
		for(int i = 0; i < inp.n; ++i) {
			getline(cin, x);
			stringstream st(x);
			st >> inp.k[i] >> inp.s[i];
		}
//		for(int i = 0; i < inp.n; ++i) {
//			getline(cin, x);
//			stringstream sa(x);
//			vector <long> v;
//			for(int j = 0; j < inp.p; ++j) {
//				long value;
//				sa >> value;
//				v.push_back(value);
//			}
//			inp.q.push_back(v);
//		}
		cout << "Case #" << l << ": ";
		printf("%.6f", solve(inp));
		cout << endl;
	}
	return 0;
}