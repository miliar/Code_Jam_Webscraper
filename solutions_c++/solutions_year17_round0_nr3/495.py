#include "string"
#include "iostream"
#include "sstream"
#include "vector"
#include "map"
#include "queue"
#include "algorithm"
#include "functional"
#include "set"
using namespace std;

#define LL long long
#define UL unsigned long long

#define VI vector<int>
#define VL vector<long long>
#define VU vector<unsigned long long>
#define VS vector<string>
#define VD vector<double>
#define VI_IT vector<int>::iterator
#define VL_IT vector<long long>::iterator
#define VU_IT vector<unsigned long long>::iterator
#define VS_IT vector<string>::iterator
#define VD_IT vector<double>::iterator

long long gap(long long n, long long k) {
	if (k == 0)
		return n;

	if ((n & 1) == 0) {
		if ((k & 1) == 0) {
			return gap((n / 2) - 1, (k - 2) / 2);
		}
		else {
			return gap(n / 2, (k - 1) / 2);
		}
	}
	else {
		if ((k & 1) == 0) {
			return gap((n - 1) / 2, (k - 2) / 2);
		}
		else {
			return gap((n - 1) / 2, (k - 1) / 2);
		}
	}
}

void doCase(int iCase) {
	printf("Case #%d: ", iCase);

	long long n, k;
	cin >> n >> k; cin.ignore(999, '\n');
	
	long long finalGap = gap(n, k - 1);
	long long max = finalGap / 2;
	long long min = (finalGap - 1) / 2;

	printf("%lld %lld\n", max, min);
}

void main(void) {
	int nCases;
	cin >> nCases;
	cin.ignore(999, '\n');

	for (int iCase = 1; iCase <= nCases; iCase++) {
		doCase(iCase);
	}
}