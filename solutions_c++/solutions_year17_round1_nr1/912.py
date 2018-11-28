#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <utility>
#include <algorithm>
using namespace std;

int const MAX_N = 256;
int const MAX_AL = 53;
int const MAX_CH = 300100;
int const INT_INF = 1000000000;

char st[MAX_CH],s[MAX_N][MAX_N];

int min_x[MAX_AL],min_y[MAX_AL],max_x[MAX_AL],max_y[MAX_AL];
int used[MAX_AL],ms[MAX_AL],ms_len = 0;
int tst,n,m;
int FL = 0;

int get_code(char x) {
	return x - 'A';
}

char get_letter(int x) {
	return 'A' + x;
}

void find_next_cell(int x, int y, int &new_x, int &new_y) {
	new_x = x; new_y = y;
	while (new_x < n && new_y < m && s[new_x][new_y] != '?') {
		new_y++;
		if (new_y >= m) {
			new_x++;
			new_y = 0;
		}
	}
}

inline int inters(int x1, int y1, int x2, int y2) {
	return max(x1,x2) <= min(y1,y2);
}

int all_ok(int idx) {
	for (int i=0; i<ms_len; i++)
		for (int j=i+1; j<ms_len; j++) {
			int a = ms[i], b = ms[j];
			if (inters(min_x[a],max_x[a],min_x[b],max_x[b]) && inters(min_y[a],max_y[a],min_y[b],max_y[b]))
				return 0;
		}
	for (int a=min_x[idx]; a<=max_x[idx]; a++)
		for (int b=min_y[idx]; b<=max_y[idx]; b++)
			if (s[a][b] != '?' && get_code(s[a][b]) != idx)
				return 0;
	return 1;
}

void rec(int x, int y) {
	if (FL == 1)
		return ;

	if (x >= n) {
		FL = 1;
		for (int i=0; i<n; i++) {
			printf("\n");
			for (int j=0; j<m; j++) printf("%c",s[i][j]);
		}
		return;
	}

	if (FL == 1)
		return;

	if (s[x][y] != '?') {
		int new_x,new_y;
		find_next_cell(x,y,new_x,new_y);
		rec(new_x,new_y);
		return;
	}

	char save_s[26][26];

	for (int vv=0; vv<ms_len; vv++) {
		int i = ms[vv];

		int our_min_x = min_x[i];
		int our_min_y = min_y[i];
		int our_max_x = max_x[i];
		int our_max_y = max_y[i];

		min_x[i] = min(min_x[i], x);
		max_x[i] = max(max_x[i], x);
		min_y[i] = min(min_y[i], y);
		max_y[i] = max(max_y[i], y);

		if (all_ok(i)) {
			for (int q=0; q<n; q++)
				for (int w=0; w<m; w++)
					save_s[q][w] = s[q][w];

			for (int a=min_x[i]; a<=max_x[i]; a++)
				for (int b=min_y[i]; b<=max_y[i]; b++)
					s[a][b] = get_letter(i);

			int new_x,new_y;
			find_next_cell(x,y,new_x,new_y);
			if (!(new_x == x && new_y == y)) {
				rec(new_x,new_y);
				if (FL == 1) return;
			}

			for (int q=0; q<n; q++)
				for (int w=0; w<m; w++)
					s[q][w] = save_s[q][w];
		}

		min_x[i] = our_min_x;
		min_y[i] = our_min_y;
		max_x[i] = our_max_x;
		max_y[i] = our_max_y;
	}
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	sscanf(st,"%d",&tst);
	for (int q=1; q<=tst; q++) {
		gets(st);
		sscanf(st,"%d%d",&n,&m);
		for (int i=0; i<MAX_AL; i++) min_x[i] = INT_INF, max_x[i] = -INT_INF, min_y[i] = INT_INF, max_y[i] = -INT_INF, used[i] = 0;
		ms_len = 0;
		for (int i=0; i<n; i++) {
			gets(st);
			for (int j=0; j<m; j++) {
				s[i][j] = st[j];
				if (s[i][j] == '?') continue;
				min_x[get_code(s[i][j])] = min(min_x[get_code(s[i][j])], i);
				max_x[get_code(s[i][j])] = max(max_x[get_code(s[i][j])], i);
				min_y[get_code(s[i][j])] = min(min_y[get_code(s[i][j])], j);
				max_y[get_code(s[i][j])] = max(max_y[get_code(s[i][j])], j);
				if (!used[get_code(s[i][j])]) {
					used[get_code(s[i][j])] = 1;
					ms[ms_len++] = get_code(s[i][j]);
				}
			}
		}

		if (q > 1) printf("\n");
		printf("Case #%d:",q);

		for (int i=0; i<MAX_AL; i++)
			if (min_x[i] < INT_INF / 2)
				for (int row = min_x[i]; row <= max_x[i]; row++)
					for (int col = min_y[i]; col <= max_y[i]; col++)
						s[row][col] = get_letter(i);

		FL = 0;
		rec(0,0);
	}
	return 0;
}
