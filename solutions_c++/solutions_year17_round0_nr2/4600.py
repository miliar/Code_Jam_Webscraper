#include <cstdio>
#include <iostream>

using namespace std;

long A[18];

void calA() {
	A[0] = 1;
	for(int i=1; i<18; i++) {
		A[i] = A[i - 1] * 10 + 1;
	}
}

long f(long x) {
	long remain = 9;
	long res = 0;
	for(int i=17; i>=0; i--) {
		long t = min(remain, x / A[i]);
		remain -= t;
		x = x % A[i];
		res += A[i] * t;
	}

	return res;
}

int main() {
	int T;
	long n;
	calA();
	cin >> T;
	for(int i=1; i<=T; i++) {
		cin >> n;
		cout << "Case #" << i << ": " << f(n) << endl;
	}
}