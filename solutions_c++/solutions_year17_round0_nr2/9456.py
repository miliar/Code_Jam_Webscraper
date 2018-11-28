#include <iostream>
#include <math.h>
#include <string>
#include <fstream>

using namespace std;
bool checkorder(string s,int l) {
	for (int i = 0; i < l-1; i++) {
		if (s[i] > s[i + 1])
			return false;
	}
	return true;
}
long long findtidy(long long n) {
	string num;
	int l;
	int i = 0;
	long long exp = 1;
	while (true) {
		num = to_string(n);
		l = num.length();

		if (l == 1) {
			return n;
		}

		if (checkorder(num, l)) {
			return n;
		}
		else {
			if (num[l-i-1] == '9') {
				i++;
				exp = exp * 10;
			}
			n = n - exp;
		}
	}
	
}

int main() {

	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("output.out");
	int t;
	input >> t;
	long long n;
	for (int i = 1; i <= t; i++) {
		input >> n ;
		long long x = findtidy(n);
		output << "Case #" << i << ": " << x << endl;
	}

	input.close();
	output.close();

	return 0;


}