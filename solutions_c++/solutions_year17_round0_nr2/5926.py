#include <iostream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <deque>
using namespace std;

bool isTidy(std::vector<int> digits) {
	unsigned s = digits.size();
	for (int i = 1; i < s; ++i) {
		if (digits[i] < digits[i - 1]) {
			return false;
		}
	}
	return true;
}

std::vector<int> getDigits(long long numer)
{
	std::deque<int> rv;
	do {
		lldiv_t res = div(numer, (long long) 10);
		rv.push_front(res.rem);
		numer = res.quot;
	} while (numer > 0);
	return std::vector<int>(rv.begin(), rv.end());
}

long long getNumer(vector<int> digits){
	long long power = 1;
	long long sum = 0;
	while (!digits.empty()) {
		int d = digits.back();
		digits.pop_back();
		sum += power*d; 
		power *= 10; 
	}
	return sum; 
}

long long createTidy(long long n) {
	std::vector<int> nDigits = getDigits(n);
	if (isTidy(nDigits)){ return n; }
	unsigned s = 1;
	long long power = 10;
	while (!isTidy(nDigits)){
		for (int i = 0; i < s; ++i) {
			nDigits.pop_back();
		} 
		long long d = getNumer(nDigits);
		d = (d - 1);
		nDigits = getDigits(d);
		for (int i = 0; i < s; ++i) {
			nDigits.push_back(9);
		}
		++s;
	}
	return getNumer(nDigits);
}

int main(void) {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
	if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
	int numCase;
	fin >> numCase;
	int i;
	long long c;
	for (i = 0; i < numCase; i++)
	{
		fin >> c;
		fout << "Case #" << (i + 1) << ": " << createTidy(c) << endl;
	}
	return 0;
}

