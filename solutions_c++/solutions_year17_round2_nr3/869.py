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

s64 N, Q, E[100], S[100], D[100][100], U[1], V[1];

struct P {
	s64 e, s;
	double t;
};

s64 Smart()
{
	return 0;
}

s64 Naive()
{
	vector<s64> dd;
	FOR(i, 1, N) dd.push_back(D[i][i + 1]);

	vector<P> v, v_new;
	P p = { E[0]-D[0][1], S[0], (double)D[0][1]/S[0] };
	v.push_back(p);
	FOR(i, 1, N-1) {
		// æ‚èŠ·‚¦‚é‚È‚çA‚±‚±‚Ü‚ÅÅ‘¬‚Å‚«‚½‚â‚Â‚©‚çB
		double t_best = 1e16;
		FOR(j, 0, v.size()) {
			if (t_best > v[j].t) {
				t_best = v[j].t;
			}
		}
		p = { E[i]-D[i][i+1], S[i], t_best + (double)D[i][i+1]/S[i] };
		if (p.e >= 0) {
			v_new.push_back(p);
		}
		// Œp‘±
		FOR(j, 0, v.size()) {
			p = { v[j].e - D[i][i + 1], v[j].s, v[j].t + (double)D[i][i + 1] / v[j].s };
			if (p.e >= 0) {
				v_new.push_back(p);
			}
		}
		v.swap(v_new);
		v_new.clear();
	}
	double t_best = 1e16;
	FOR(j, 0, v.size()) {
		if (t_best > v[j].t) {
			t_best = v[j].t;
		}
	}
	cout << t_best << endl;
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
		cin >> N >> Q;
		FOR(i, 0, N) cin >> E[i] >> S[i];
		FOR(i, 0, N) FOR(j, 0, N) cin >> D[i][j];
		FOR(i, 0, Q) cin >> U[i] >> V[i];
		Naive();
	}

	return 0;
}
