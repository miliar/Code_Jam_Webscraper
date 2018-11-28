#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

int findcutoff(const vector<int> &digits) {
	int n = (int)digits.size();
	int cut = n-1;
	for(int i=n-2; i>=0; i--) {
		if(digits[i]>digits[cut])
			cut = i;
		else if(digits[i]<digits[cut])
			return cut;
	}
	return -1;
}

long long lastnum(long long n) {
	vector<int> digits;
	while(n>0) {
		digits.push_back(n%10);
		n /= 10;
	}
	int cut = findcutoff(digits);
	long long m = 0;
	for(int i=(int)digits.size()-1; i>=0; i--) {
		m *= 10;
		if(i>cut)
			m += digits[i];
		else if(i<cut)
			m += 9;
		else
			m += digits[i]-1;
	}
	return m;
}

int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		long long N;
		fin >> N;
		long long M = lastnum(N);
		fout << "Case #" << t << ": " << M << endl;
	}

	return 0;
}

