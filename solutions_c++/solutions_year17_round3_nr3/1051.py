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

s64 N, K, P[50], U, D=10000000000000LL;

s64 Smart()
{

	return 0;
}

s64 Naive()
{
	while (U > 0) {
		vector<int> v;
		s64 p_min = 10*D, p_sec = 10*D;
		FOR(i, 0, N) {
			if (P[i] < p_min) {
				v.clear();
			}
			if (P[i] <= p_min) {
				p_min = P[i];
				v.push_back(i);
			}
		}
		FOR(i, 0, N) {
			if (P[i] == p_min) continue;
			if (P[i] <= p_sec) {
				p_sec = P[i];
			}
		}
		s64 u = MIN(U, v.size()*(p_sec - p_min));
		FOR(i, 0, v.size()) {
			P[v[i]] += u / v.size();
		}
		U -= u;
	}
	double a = 1.0;
	FOR(i, 0, N) {
		a *= (double)P[i] / D;
	}
	cout << fixed << a << endl;
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
	double d;
	FOR (tt,0,num_of_trial) {
		cout << "Case #" << tt+1 << ": ";
		cin >> N >> K >> d;
		U = (s64)(D * d);
		FOR(i, 0, N) {
			cin >> d;
			P[i] = (s64)(D * d);
		}
		s64 ans = Naive();
	}

	return 0;
}
