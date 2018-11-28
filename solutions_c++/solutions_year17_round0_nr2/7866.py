#include<iostream>
#include<fstream>

using namespace std;

long long int digit(long long int n, int d) {
	long long  int b = 1;
	for (int i = 0; i < d; i++) b *= 10;
	n /= b;
	return n % 10;
}

long long int ans(long long int n) {
	if (n < 10) return n;

	long long int d, b = 1;
	for (d = 0; b <= n; d++) b *= 10;

	d--;
	b /= 10;

	while (d >= 1 && digit(n, d) <= digit(n, d - 1)) {
		d--;
		b /= 10;
	}

	if (d == 0) return n;
	return ans((n / b) * b - 1);
}

int main(void) {
	int T;
	ifstream inputfile("B-small-attempt0.in");
	ofstream outputfile("out.txt");

	inputfile >> T;

	for (int t = 1; t <= T; t++) {
		long long N;
		inputfile >> N;
		outputfile << "Case #" << t << ": " << ans(N) << endl;
	}

	system("pause");
	return 0;
}