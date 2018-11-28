#include <stdio.h>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
//#include "windows.h"
//#include "../../gmp_int.h"
//#include "../../common.h"
#define MAX(a, b)		((a)>(b)?(a):(b))
#define MIN(a, b)		((a)<(b)?(a):(b))
#define MAX3(a, b, c)	(MAX((a),MAX((b),(c))))
#define FOR(a,b,c)		for (s32(a)=(b);(a)<(s32)(c);(a)++)
#define BL				{char bl[10];cin.getline(bl, 10);}
#define GL(c)			cin.getline(c, sizeof(c))
typedef char					s8;
typedef unsigned char			u8;
typedef short					s16;
typedef unsigned short			u16;
typedef int						s32;
typedef unsigned int			u32;
typedef long long int			s64;
typedef unsigned long long int	u64;
using namespace std;

ifstream test_input;
#define cin test_input

s64 N, K, R[20], H[20];
double PI = 3.1415926535897932384626433832795;

struct S {
	s64 r, h, i;
};

bool operator < (const S &s1, const S &s2) {
	return s1.r < s2.r;
}

s64 Smart()
{

	return 0;
}

s64 Naive()
{
	vector<int> v;
	FOR(i, 0, N) v.push_back(i);
	s64 a_max = 0;
	do {
		bool ok = true;
		FOR(i, 0, MIN(N - 1, K - 1)) {
			int j = v[i], k = v[i+1];
			if (R[j] < R[k]) ok = false;
		}
		if (ok) {
			s64 a = R[v[0]]*R[v[0]];
			FOR(i, 0, K) {
				int j = v[i];
				a += 2 * R[j] * H[j];
			}
			if (a_max < a) {
				//FOR(i, 0, K) cout << v[i].r << " ";
				//cout << endl;
				a_max = a;
			}
		}
	} while (next_permutation(v.begin(), v.end()));
	cout << PI*a_max << endl;
	return 0;
}

int main(int argc, char* argv[])
{
	cout.precision(15);
	if (argc!=2) {
		cout << "Need input file name." << endl;
		return 0;
	}
	test_input.open(argv[1]);
	if (test_input.fail()) {
		cout << "Cannot open input file " << argv[1] << "." << endl;
		return 0;
	}

	s32 num_of_trial;
	cin >> num_of_trial;
	FOR (tt,0,num_of_trial) {
		cout << "Case #" << tt+1 << ": ";
		cin >> N >> K;
		FOR(i, 0, N) cin >> R[i] >> H[i];
		s64 ans = Naive();
	}

	return 0;
}
