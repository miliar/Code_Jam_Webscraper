#include <iostream>
#include <fstream>
using namespace std;

int numDigits(long long num)
{
	int digits = 0;
	double N = num;
	while (N) {
		N = floor(N / 10);
		digits++;
	}
	return digits;
}

long long tidy(long long N, int min, int digits) {
	if (digits == 0) {
		if (N >= min) return N;
		else return -1;
	}

	//int last;
	//int digits = numDigits(N, last) - 1;
	long long p = pow(10, digits);
	long long m = N % p;
	int last = (N - m) / p;
	if (last < min) return -1;

	long long res = tidy(m, last, digits - 1);
	if (res > -1) return res + last * p;

	for (int l = last - 1; l >= min; l--) {
		res = tidy(p - 1, l, digits - 1);
		if (res > -1) return res + l * p;
	}
}

int main() {
	ifstream infile("in22.in");
	ofstream out("out22.txt");
	int T;
	infile >> T;

	for (int t = 0; t < T; t++) {
		long long N;
		infile >> N;

		int dig = numDigits(N);

		out << "Case #" << t + 1 << ": " << tidy(N, 0, dig - 1) << endl;
	}

	system("pause");
	return 0;
}