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

s64 AC, AJ, C[5], D[5], J[5], K[5];

s64 Smart()
{

	return 0;
}

void Swap(s64 &x, s64 &y) {
	s64 t = x;
	x = y;
	y = t;
}

s64 Naive()
{
	if (AC + AJ == 1) {
		return 2;
	}
	if (AC == 2) {
		if (C[0] > C[1]) {
			Swap(C[0], C[1]);
			Swap(D[0], D[1]);
		}
		if (D[1] - C[0] <= 720) return 2;
		if (1440 + D[0] - C[1] <= 720) return 2;
		return 4;
	}
	if (AJ == 2) {
		if (J[0] > J[1]) {
			Swap(J[0], J[1]);
			Swap(K[0], K[1]);
		}
		if (K[1] - J[0] <= 720) return 2;
		if (1440 + K[0] - J[1] <= 720) return 2;
		return 4;
	}
	return 2;
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
		cin >> AC >> AJ;
		FOR(i, 0, AC) cin >> C[i] >> D[i];
		FOR(i, 0, AJ) cin >> J[i] >> K[i];
		s64 ans = Naive();
		cout << ans << endl;
	}

	return 0;
}
