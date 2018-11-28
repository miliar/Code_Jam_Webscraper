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
	cin >> s; cin.ignore(999, '\n');

	int stopper = s.length();
	for (int i = s.length() - 2; i >= 0; i--) {
		if (s[i] > s[i + 1]) {
			for (int j = i + 1; j < stopper; j++)
				s[j] = '9';
			s[i] = s[i] - 1;
			stopper = i + 1;
		}
	}

	while (s[0] == '0')
		s.erase(0, 1);

	printf("%s\n", s.c_str());
}

void main(void) {
	int nCases;
	cin >> nCases;
	cin.ignore(999, '\n');

	for (int iCase = 1; iCase <= nCases; iCase++) {
		doCase(iCase);
	}
}