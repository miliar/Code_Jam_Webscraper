#include "stdafx.h"
#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int T;
long long N;
long long K;
long long y;
long long z;

void stall(long long N, long long K) {
	int i = 0;
	long long l = 0;
	while (K > pow(2, i)) {
		l += pow(2, i);
		K -= pow(2, i);
		i++;
	}
	long long left = N - l;
	long long units = pow(2, i);
	long long d = left / units;
	long long m = left%units;
	if (K <= m)d = d + 1;
	z = (d - 1) / 2; y = (d - 1) - z;
}
int main() {
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> N >> K;
		stall(N, K);
		cout << "Case #" << i << ": " << y << " " << z << endl;
	}
	return 0;
}