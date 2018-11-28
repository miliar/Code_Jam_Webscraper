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

int R, C;
int D[100][100];
char E[100][100];
vector<int> X, Y;
vector<char> S;

s64 Smart()
{
	set<char> used;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (E[i][j] == '?') continue;
			if (used.find(E[i][j]) != used.end()) continue;
			used.insert(E[i][j]);
			int p, q;
			for (p = j; p >= 0; p--) {
				if (E[i][p] == '?' || E[i][p] == E[i][j]) E[i][p] = E[i][j];
				else break;
			}
			p ++;
			for (q = j+1; q < C; q++) {
				if (E[i][q] == '?' || E[i][q] == E[i][j]) E[i][q] = E[i][j];
				else break;
			}
			q--;
			for (int k = i - 1; k >= 0; k--) {
				bool ok = true;
				for (int r = p; r <= q; r++) {
					if (E[k][r] != '?') {
						ok = false;
						break;
					}
				}
				if (ok) {
					for (int r = p; r <= q; r++) E[k][r] = E[i][j];
				}
				else break;
			}
			for (int k = i+1; k < R; k++) {
				bool ok = true;
				for (int r = p; r <= q; r++) {
					if (E[k][r] != '?') {
						ok = false;
						break;
					}
				}
				if (ok) {
					for (int r = p; r <= q; r++) E[k][r] = E[i][j];
				}
				else break;
			}
			//for (int p = 0; p < R; p++) {
			//	for (int q = 0; q < C; q++) {
			//		cout << E[p][q];
			//	}
			//	cout << endl;
			//}
			//cout << endl;
		}
	}
	cout << endl;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cout << E[i][j];
		}
		cout << endl;
	}
	return 0;
}

s64 Naive()
{
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			D[i][j] = -1;
		}
	}
	vector<pair<int, int>> p, q;
	p.push_back(pair<int, int>(0, 0));
	q.push_back(pair<int, int>(R - 1, C - 1));
	for (int k = 0; k < X.size(); k++) {
		pair<int, int> p_new, q_new;
		int l;
		if (k == 0) l = D[Y[k]][X[k]];
		if (p[l].second == q[l].second) {
			p_new.first = Y[k];
			p_new.second = p[l].second;
			q_new.first = q[l].first;
			q_new.second =	q[l].second;
			q[l].first = Y[k] - 1;
		}
		else {
			p_new.first = p[l].first;
			p_new.second = X[k];
			q_new.first = q[l].first;
			q_new.second = q[l].second;
			q[l].second = X[k] - 1;
		}
		for (int i = p_new.first; i <= q_new.first; i++) {
			for (int j = p_new.second; j <= q_new.second; j++) {
				D[i][j] = k;
			}
		}
		//for (int i = 0; i < R; i++) {
		//	for (int j = 0; j < C; j++) {
		//		cout << D[i][j];
		//	}
		//	cout << endl;
		//}
		//cout << endl;
		p.push_back(p_new);
		q.push_back(q_new);
	}
	cout << endl;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cout << S[D[i][j]];
		}
		cout << endl;
	}
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
		cin >> R >> C;
		X.clear();
		Y.clear();
		S.clear();
		for (int i = 0; i < R; i++) {
			string s;
			cin >> s;
			for (int j = 0; j < C; j++) {
				E[i][j] = s[j];
				if (s[j] != '?') {
					Y.push_back(i);
					X.push_back(j);
					S.push_back(s[j]);
				}
			}
		}
		s64 ans = Smart();
	}

	return 0;
}
