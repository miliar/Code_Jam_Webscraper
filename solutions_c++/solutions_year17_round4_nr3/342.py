#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

#define MAXCODE 1024

int tn, R, C;
char a[6][100];
int f[100][MAXCODE]; // 0-242 if possible; -1 if not possible
string g[100][MAXCODE]; // the true layout
char sol[6][100];

vector<string> candidates;

inline int char2int(char c) {

	switch (c) {
		case '#': return 0;
		case '-': return 1;
		case '|': return 2;
		case '.': return 3;
	}

	fprintf(stderr, "Oops, c=%c encountered\n", c);
	exit(0);

}

inline char int2char(int x) {

	switch (x) {
		case 0: return '#';
		case 1: return '-';
		case 2: return '|'; 
		case 3: return '.';
	}

	fprintf(stderr, "Ooops, x=%d encountered\n", x);
	exit(0);

}

int tocode(string a) {

	int ret = 0;
	int base = 1;
	for(int i = 0; i < R; i++) {
		ret += char2int(a[i]) * base;
		base *= 4;
	}

	return ret;

}

string tostring(int code) {

	string ret = "";
	for(int i = 0; i < R; i++) {
		ret = ret + int2char(code%4);
		code /= 4;
	}

	return ret;

}

void build_candidates(int c) {

	candidates.clear();
	for(int mask = 0; mask < (1<<R); mask ++) {
		string s = "";
		for(int i = 0; i < R; i++) {
			if (a[i][c] == '#' || a[i][c] == '.' || (mask & (1<<i)) == 0)
				s = s + a[i][c];
			else if (a[i][c] == '-')
				s = s + '|';
			else
				s = s + '-';
		}
		candidates.push_back(s);
	}

}

void find_solution(int final_code) {

	int t = final_code;
	for(int j = C-1; j > 0; j--) {
		string s = g[j][t];
		for(int i = 0; i < R; i++)
			sol[i][j] = s[i];
		t = f[j][t];
	}

}

string check_feasible(string x, string y) {

	//printf("x = %s, y = %s\n", x.c_str(), y.c_str());
	string z = y;

	// no self destroy in z
	int i = 0;
	while (i < R) {
		if (z[i] == '|') {
			int j = i-1;
			while (j >= 0 && z[j] != '#') {
				if (z[j] != '.') return "NO";
				z[j--] = '|';
			}
			j = i + 1;
			while (j < R && z[j] != '#') {
				if (z[j] != '.') return "NO";
				z[j++] = '|';
			}
			i = j + 1;
		}
		else i ++;
	}

	// no destroy from x to z or z to x
	for(int i = 0; i < R; i++) {
		if (x[i] == '-') {
			if (z[i] != '.' && z[i] != '#') return "NO";
			if (z[i] == '.') z[i] = '-';
		}
		else if (z[i] == '-') {
			if (x[i] != '#' && x[i] != '.') return "NO";
		}
	}

	// no hiding .
	for(int i = 0; i < R; i++)
		if (x[i] == '.' && (z[i] == '#' || z[i] == '|')) return "NO";

	for(int i = 0; i < R; i++)
		if (x[i] == '|' && z[i] == '.') return "NO";

	// check there is no "." remaining in z
	/*for(int i = 0; i < R; i++)
		if (z[i] == '.') return "NO";*/

	//printf("z = %s\n", z.c_str());
	return z;

}

int main() {

	scanf("%d\n", &tn);

	for(int ctn = 0; ctn < tn; ctn ++) {

		scanf("%d %d\n", &R, &C);
		C = C + 2;
		for(int i = 0; i < R; i++) {
			a[i][0] = '#';
			for(int j = 1; j < C-1; j++) {
				scanf("%c", &a[i][j]);
			}
			a[i][C-1] = '#';
			scanf("\n");
		}

		/*for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				printf("%c", a[i][j]);
			}
			printf("\n");
		}*/

		for(int i = 0; i < C; i++)
			for(int j = 0; j < MAXCODE; j++)
				f[i][j] = -1;
		f[0][0] = 0;
		g[0][0] = "";
		g[C-1][0] = "#######";

		for(int i = 1; i < C; i++) {
			build_candidates(i);
			//printf("i = %d\n", i);
			/*for(int k = 0; k < MAXCODE; k++)
				if (f[i-1][k] >= 0) printf("i = %d, s = %s\n", i, tostring(k).c_str());*/
			for(int j = 0; j < candidates.size(); j++) {
				//printf("candidate: %s\n", candidates[j].c_str());
				for(int k = 0; k < MAXCODE; k++) {
					if (f[i-1][k] < 0) continue;
					string new_candidate = check_feasible(tostring(k), candidates[j]);
					//printf("k = %s, candidate = %s, new_candidate = %s\n", tostring(k).c_str(), candidates[j].c_str(), new_candidate.c_str());
					if (new_candidate != "NO") {
						int t = tocode(new_candidate);
						f[i][t] = k;
						g[i][t] = candidates[j];
					}
				}
			}
			//puts("===============================");
		}


		printf("Case #%d: ", ctn+1);
		if (f[C-1][0] < 0) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("POSSIBLE\n");
			find_solution(0);
			for(int i = 0; i < R; i++) {
				for(int j = 1; j < C-1; j++)
					printf("%c", sol[i][j]);
				printf("\n");
			}
		}

	}

	return 0;

}