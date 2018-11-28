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

s64 R, O, Y, G, B, V, N;
s64 Smart()
{
	return 0;
}

string replace(string String1, string String2, string String3) {
	string::size_type  Pos(String1.find(String2));
	while (Pos != string::npos) {
		String1.replace(Pos, String2.length(), String3);
		Pos = String1.find(String2, Pos + String3.length());
	}
	return String1;
}

s64 Naive()
{
	if (V > Y || G > R || O > B) {
		cout << "IMPOSSIBLE" << endl;
		return 0;
	}
	Y -= V;
	R -= G;
	B -= O;
	s64 m = MAX3(R, Y, B);
	if (m > (N - 2 * (V + G + O)) / 2) {
		cout << "IMPOSSIBLE" << endl;
		return 0;
	}
	string s;
	s64 p = -1; // RYB
	FOR(i, 0, N-2*(V+G+O)) {
		if (p == -1) {
			if (R >= Y && R >= B) {
				s += "R";
				R--;
				p = 0;
			}
			else if (Y >= B) {
				s += "Y";
				Y--;
				p = 1;
			}
			else {
				s += "B";
				B--;
				p = 2;
			}
		}
		else if (p == 0) { // R
			if (Y >= B) {
				s += "Y";
				Y--;
				p = 1;
			}
			else {
				s += "B";
				B--;
				p = 2;
			}
		}
		else if (p == 1) { // Y
			if (R >= B) {
				s += "R";
				R--;
				p = 0;
			}
			else {
				s += "B";
				B--;
				p = 2;
			}
		}
		else if (p == 2) { // B
			if (R >= Y) {
				s += "R";
				R--;
				p = 0;
			}
			else {
				s += "Y";
				Y--;
				p = 1;
			}
		}
	}
	if (!s.empty() && s[0] == s[s.size() - 1]) {
		s = s.substr(0, s.size() - 2) + s[s.size() - 1] + s[s.size() - 2];
	}
	if (G > 0) {
		string::size_type i = s.find_first_of("R");
		string t = "";
		FOR(j, 0, G) t += "RG";
		if (s.empty()) s = t;
		else {
			if (i == string::npos) {
				cout << "IMPOSSIBLE" << endl;
				return 0;
			}
			s = s.substr(0, i) + t + s.substr(i);
		}
	}
	if (O > 0) {
		string::size_type i = s.find_first_of("B");
		string t = "";
		FOR(j, 0, O) t += "BO";
		if (s.empty()) s = t;
		else {
			if (i == string::npos) {
				cout << "IMPOSSIBLE" << endl;
				return 0;
			}
			s = s.substr(0, i) + t + s.substr(i);
		}
	}
	if (V > 0) {
		string::size_type i = s.find_first_of("Y");
		string t = "";
		FOR(j, 0, V) t += "YV";
		if (s.empty()) s = t;
		else {
			if (i == string::npos) {
				cout << "IMPOSSIBLE" << endl;
				return 0;
			}
			s = s.substr(0, i) + t + s.substr(i);
		}
	}
	cout << s << endl;
	if (s.size() != N) {
		cout << "!";
	}
	// test
	s = replace(s, "R", "1");
	s = replace(s, "Y", "2");
	s = replace(s, "O", "3");
	s = replace(s, "B", "4");
	s = replace(s, "V", "5");
	s = replace(s, "G", "6");
	FOR(i, 0, s.size()) {
		int x = s[i] - '0', y = s[(i + 1)%N] - '0';
		if ((x & y) != 0) {
			cout << "!";
		}
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
		cout << "Case #" << tt + 1 << ": ";
		//R = RAND(0, 10);
		//O = RAND(0, 10);
		//Y = RAND(0, 10);
		//G = RAND(0, 10);
		//B = RAND(0, 10);
		//V = RAND(0, 10);
		//N = R + O + Y + G + B + V;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		Naive();
	}

	return 0;
}
