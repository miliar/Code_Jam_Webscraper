#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("2.in");
ofstream fout("2.out");

bool proc(const char* d, int cnt, char* s) {
	if (cnt == 0)
		return false;

	int offset = 0;
	const int len = strlen(s);
	char newS[1001];
	for (int i = 0; i < len+1; i++) {

		if(s[i] == d[0] && offset == 0) {
			offset = 2 * cnt;
			for (int j = 0; j < 2 * cnt; j++) {
				newS[i + j] = d[j % 2];
			}
		}

		newS[i + offset] = s[i];
	}

	if (offset != 0) {
		strcpy(s, newS);
		return false;
	}

	if (len == 0) {
		for (int j = 0; j < 2 * cnt; j++) {
			s[j] = d[j % 2];
		}
		s[2 * cnt] = '\0';
		return false;
	}
	
	return true;
}

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fout << "Case #" << t << ": ";
		int N, R, O, Y, G, B, V;
		fin >> N >> R >> O >> Y >> G >> B >> V;
		int origN = N;
		
		R -= G;
		Y -= V;
		B -= O;
		N = R + Y + B;

		if (R < 0 || Y < 0 || B < 0) {
			fout << "IMPOSSIBLE" << endl;
			continue;
		}

		char s[1001];
		vector<pair<int, char>> pr = { {R,'R'}, {Y,'Y'}, {B,'B'} };
		sort(pr.begin(), pr.end());
		int n2 = N - 2 * pr[2].first;
		int n1 = pr[2].first - n2;

		if(n1 < 0 || n2 < 0){
			fout << "IMPOSSIBLE" << endl;
			continue;
		}

		int cur = 0;
		for (int i = 0; i < pr[2].first; i++) {
			s[cur++] = pr[2].second;
			if (n2-- > 0) {
				s[cur++] = pr[0].second;
				s[cur++] = pr[1].second;
				pr[0].first--;
				pr[1].first--;
			}
			else {
				if(pr[1].first-- > 0)
					s[cur++] = pr[1].second;
				else if (pr[0].first-- > 0)
					s[cur++] = pr[0].second;
				else
					assert(false);
			}

		}
		s[N] = '\0';
		
		if(proc("RG", G, s) || proc("YV", V, s) || proc("BO", O, s)) {
			fout << "IMPOSSIBLE" << endl;
			continue;
		}

		fout << s << endl;

		int c[] = { 0,0,0, 0,0,0 };
		for (int i = 0; i < strlen(s); i++) {
			if (s[i] == 'R')
				c[0]++;
			else if (s[i] == 'Y')
				c[1]++;
			else if (s[i] == 'B')
				c[2]++;
			else if (s[i] == 'O')
				c[3]++;
			else if (s[i] == 'G')
				c[4]++;
			else if (s[i] == 'V')
				c[5]++;
			assert(s[i] != s[(i + 1) % origN]);
		}
		assert(c[0] == R + G);
		assert(c[1] == Y + V);
		assert(c[2] == B + O);
		assert(c[3] == O);
		assert(c[4] == G);
		assert(c[5] == V);
	}
	return 0;
}
