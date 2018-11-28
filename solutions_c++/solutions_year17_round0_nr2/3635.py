#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

unsigned long long tidyup(unsigned long long n) {
	unsigned long long i = 1;
	
	bool tidy = true;
	while (n / i > 0) {
		unsigned long long m = n/i;
		unsigned long long a = m % 10;
		unsigned long long b = (m / 10) % 10;
		if (b > a) {
			n = (m / 10) * 10 * i - 1;
			tidy = false;
		}
		i = i*10;
	}

	if (!tidy)
		return tidyup(n);

	return n;
}

int main()
{
	ifstream a("D:\\gcj\\example.txt");
	ofstream o("D:\\gcj\\output.txt");
	int nr; a >> nr;
	std::string line;
	//std::getline(a, line);
	string r("");
	for (int ii = 0; ii<nr; ii++) {
		o << "Case #" << (ii + 1) << ": ";
		cout << "Case #" << (ii + 1) << ": ";
		
		unsigned long long n; a >> n;
		
		n = tidyup(n);

		o << n << endl;
		cout << n << endl;
	}
	a.close();
	o.close();
	char c; cin >> c;
	return 0;
}

