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
#include "windows.h"
//#include "../../gmp_int.h"
//#include "../../common.h"
#define MAX(a, b)		((a)>(b)?(a):(b))
#define MAX3(a, b, c)	(MAX((a),MAX((b),(c))))
#define FOR(a,b,c)		for (s32(a)=(b);(a)<(s32)(c);(a)++)
#define BL				{char bl[10];cin.getline(bl, 10);}
#define GL(c)			cin.getline(c, sizeof(c))
#define RAND(a,b)		((a)+(s32)(rand()*((b)-(a)+1.0)/(1.0+RAND_MAX)))
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

s64 N, K;

struct S {
	s64 d, c;
};
//
//bool operator

void Smart()
{
	map<s64, s64> m;
	m[N] = 1;
	s64 k = 0;
	while (true) {
		s64 p = m.rbegin()->first, q = m.rbegin()->second;
		m.erase(p);
		k += q;
		if (k >= K) {
			cout << p / 2 << " ";
			if (p % 2 == 0) cout << p / 2 - 1 << endl;
			else cout << p / 2 << endl;
			break;
		}
		if (p % 2 == 1) {
			m[p / 2] += 2 * q;
		}
		else {
			m[p / 2] += q;
			m[p / 2 - 1] += q;
		}
	}
}

void Naive()
{
	int lr_max, lr_min;
	vector<bool> v(N+2);
	v[0] = v[v.size() - 1] = true;
	for (int i = 0; i < K; i++) {
		int c = 0, c_max = 0, j_max = -1;
		for (int j = 0; j < N + 1; j++) {
			if (v[j]) {
			} else {
				c++;
				if (v[j + 1]) {
					if (c_max < c) {
						c_max = c;	j_max = j;
					}
					c = 0;
				}
			}
		}
		v[j_max - c_max / 2] = 1;
		lr_max = lr_min = c_max / 2;
		if (c_max % 2 == 0) lr_min --;
		//cout << endl << c_max << " " << lr_max << " " << lr_min;
	}
	cout << lr_max << " " << lr_min << endl;
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
		Smart();
		//Naive();
	}

	return 0;
}
