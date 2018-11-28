#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;

FILE* in = freopen("date.in", "r", stdin);
FILE* out = freopen("date.out", "w", stdout);
unsigned long long n, k;
int T;
unsigned long long  log2(unsigned long long  int number);
int main()
{

	
	cin >> T;
	for (int test = 1; test <= T; test++)
	{
		cin >> n >> k;
		unsigned long long  logarithm = log2(k);
		// beginning of the row
		unsigned long long  freeStalls = n - (1LL << logarithm) + 1;
		unsigned long long  thisRow = 1LL << logarithm;
		unsigned long long a, b, rest;
		a = freeStalls / thisRow; // this is the lower number;
		rest = freeStalls % thisRow; // this is how many of the Bigger ones we have
		b = a + 1;
		unsigned long long  stalls;
		if (k > thisRow + rest - 1)
			stalls = a;
		else
			stalls = b;
		
		unsigned long long  minim, maxim;
		if (stalls % 2 == 0) {
			minim = stalls / 2 - 1;
			maxim = stalls / 2;
		}
		else {
			minim = maxim = (stalls - 1) / 2;
		}

		cout << "Case #" << test << ": " << maxim << " " << minim << '\n';
	}
	return 0;
}
unsigned long long  log2(unsigned long long  int number) {
	unsigned long long  logarithm = 0;
	while (number = (number >> 1))
		logarithm++;
	return logarithm;
}