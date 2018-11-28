#include "string" 
#include "iostream"
#include "sstream"
#include "vector"
#include "map"
#include "queue"
#include "algorithm"
#include "functional"
#include "set"
#include "tuple"
using namespace std;

#define LL long long
#define UL unsigned long long

#define VC vector<char>
#define VI vector<int>
#define VU vector<unsigned int>
#define VL vector<long long>
#define VUL vector<unsigned long long>
#define VS vector<string>
#define VD vector<double>
#define VB vector<bool>
#define VC_IT VC::iterator;
#define VI_IT VI::iterator
#define VU_IT VU::iterator
#define VL_IT VL::iterator
#define VUL_IT VUL::iterator
#define VS_IT VS::iterator
#define VD_IT VD::iterator
#define VB_IT VB::iterator;

string questions = "?????????????????????????";

void fill(char ch, vector<string>& cake, int t, int l, int R, int C) {
	for (int r = t; r < R; r++)
		for (int c = l; c < C; c++)
			cake[r][c] = ch;
}

void assign(vector<string>& cake, int t, int l, int R, int C) {
	if (R == t || C == l)
		return;

	for (int r = t; r < R; r++) {
		for (int c = l; c < C; c++) {
			if (cake[r][c] != '?') {
				char ch = cake[r][c];
				// skip to next letter on this row
				while (++c < C)
					if (cake[r][c] != '?')
						break;

				// extend the rectangle down as far as possible
				while (++r < R) {
					if (cake[r].substr(l, c - l) != questions.substr(0, c - l))
						break;
				}

				// fill it
				fill(ch, cake, t, l, r, c);

				// do the right hand side if any
				if (c < C)
					assign(cake, t, c, r, C);

				// do the bottom if any
				if (r < R) {
					assign(cake, r, l, R, C);
				}

				return;
			}
		}
	}
	fprintf(stderr, "Failed at %d, %d, %d, %d\n", t, l, R, C);
}

void doCase(int iCase) {
	printf("Case #%d:\n", iCase);

	int R, C;
	cin >> R >> C; cin.ignore(999, '\n');

	vector<string> cake;
	for (int i = 0; i < R; i++) {
		string s;
		cin >> s; cin.ignore(999, '\n');
		cake.push_back(s);
	}

	assign(cake, 0, 0, R, C);

	for (int i = 0; i < R; i++) {
		printf("%s\n", cake[i].c_str());
	}
}

void main(void) {
	int nCases;
	cin >> nCases;
	cin.ignore(999, '\n');

	for (int iCase = 1; iCase <= nCases; iCase++) {
		doCase(iCase);
	}
}