#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

#define LL long long

int T, nCase;
LL N;

LL f(LL x)
{
	LL base = 1;
	LL b = 10;
	while (x) {
		if (x%10 > b) return base;
		b = x%10;
		x/=10;
		base *= 10;
	}
	return 0;
}

LL solv()
{
	LL p = 0;
	while (0 != (p = f(N))) {
		N = N - N % p - 1;
	}
	return N;
}

int main ()
{
	cin >> T;
	for (nCase = 1; nCase <= T; ++nCase) {
		cin >> N;
		cout << "Case #" << nCase << ": " << solv() << endl;
	}
	return 0;
}