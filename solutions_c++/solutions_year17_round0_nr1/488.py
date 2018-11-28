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

void doCase(int iCase) {
	printf("Case #%d: ", iCase);

	string s;
	int k;
	cin >> s >> k;
	cin.ignore(999, '\n');

	int n = s.length();
	int nFlips = 0;
	for (int i = 0; i < n - k + 1; i++) {
		if (s[i] == '-') {
			for (int j = i; j < i + k; j++) {
				if (s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
			nFlips++;
		}
	}

	bool didIt = true;
	for (int i = n - k + 1; i < n; i++)
		if (s[i] == '-')
			didIt = false;

	if (!didIt)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", nFlips);
}

void main(void) {
	int nCases;
	cin >> nCases;
	cin.ignore(999, '\n');

	for (int iCase = 1; iCase <= nCases; iCase++) {
		doCase(iCase);
	}
}