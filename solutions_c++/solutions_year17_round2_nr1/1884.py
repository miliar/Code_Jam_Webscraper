#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define ll long long

int main() {

	std::ifstream in("C:/Users/Yoav/Documents/Visual Studio 2015/Projects/20171b/20171b/A-large.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("C:/Users/Yoav/Documents/Visual Studio 2015/Projects/20171b/20171b/A-large.out");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	std::cout.precision(50);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		ll d, n;
		cin >> d >> n;
		ll k, s;
		double lt = 0;
		for (int i = 0; i < n; i++) {
			cin >> k >> s;
			double time = (d - (double)k) / s;
			if (time > lt)
				lt = time;
		}
		cout << d / lt << endl;

	}
	return 0;
}