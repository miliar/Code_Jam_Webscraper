#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <map>
using namespace std;

char arr[25][25];

struct dim {
	int r1;
	int c1;
	int r2;
	int c2;
};

struct dim findrect(char ch, int occur, int r, int c)
{
	int minr, minc, maxr, maxc;
	minr = minc = 26;
	maxr = maxc = -1;

	struct dim rc = { 0 };
	if (occur == 1)
		for (int x = 0; x < r; x++) {
			for (int y = 0; y < c; y++) {
				if (arr[x][y] == ch) {
					rc.c1 = rc.c2 = y;
					rc.r1 = rc.r2 = x;
				}
			}
		}
	else {
		for (int x = 0; x < r; x++) {
			for (int y = 0; y < c; y++) {
				if (arr[x][y] == ch) {
					if (minr > x) minr = x;
					if (minc > y) minc = y;
					if (maxr < x) maxr = x;
					if (maxc < y) maxc = y;
				}
			}
		}

		rc.c1 = minc;
		rc.c2 = maxc;
		rc.r1 = minr;
		rc.r2 = maxr;
	}

	return rc;

}

void fillrect(char ch, struct dim rc, int r, int c)
{
	if (rc.r1 == rc.r2 && rc.c1 == rc.c2)
	{
		int y = rc.c1;
		for (int x = rc.r1; x < r; x++) {
			if (arr[x][y] != '?')
				break;
			arr[x][y] = ch;
		}
		return;
	}

	for (int x = rc.r1; x <= rc.r2; x++) {
		for (int y = rc.c1; y <= rc.c2; y++) {
			arr[x][y] = ch;
		}
	}
}

void fillremain(int r, int c)
{
	int x, y;

	for (x = 0; x < r; x++) {
		for (y = 0; y < c; y++) {
			if (arr[x][y] == '?') {
				if (x-1 >= 0)
					arr[x][y] = arr[x-1][y];
				
			}
		}
	}

	for (x = r-1; x >= 0; x--) {
		for (y = 0; y < c; y++) {
			if (arr[x][y] == '?') {
				if (x + 1 < r)
					arr[x][y] = arr[x + 1][y];

			}
		}
	}
}

void fillremaincol(int r, int c)
{
	int x, y;

	for (x = 0; x < r; x++) {
		for (y = 0; y < c; y++) {
			if (arr[x][y] == '?') {
				if (y + 1 <= c - 1 && arr[x][y + 1] != '?') arr[x][y] = arr[x][y+1];
				else if (y - 1 >= 0 && arr[x][y - 1] != '?') arr[x][y] = arr[x][y-1];
			}
		}
	}
}

void fillremaincol2(int r, int c)
{
	int x, y;

	for (x = 0; x < r; x++) {
		for (y = c-1; y >= 0; y--) {
			if (arr[x][y] == '?') {
				if (y + 1 <= c - 1 && arr[x][y + 1] != '?') arr[x][y] = arr[x][y + 1];
				else if (y - 1 >= 0 && arr[x][y - 1] != '?') arr[x][y] = arr[x][y - 1];
			}
		}
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("Acake-large.out", "w", stdout);

	int r, c, ls, rs;
	int t, i, j, x, y;
	bool quespres = false;

	scanf("%d", &t);

	for (i = 1; i <= t; i++) {

		scanf("%d%d\n", &r, &c); 
		map<char, int> alpha;
		quespres = false;
		memset(arr, 0, sizeof(char) * 25 * 25);

		for (x = 0; x < r; x++) {
			for (y = 0; y < c; y++) {
				scanf("%c", &arr[x][y]);
				if (arr[x][y] == '?')
					quespres = true;
				else
					alpha[arr[x][y]] += 1;
			}
			if (x != r-1) scanf("\n");
		}

		if (quespres == true) {
			for (std::map<char, int>::iterator it = alpha.begin(); it != alpha.end(); ++it) {
				struct dim rc = findrect(it->first, it->second, r, c);
				fillrect(it->first, rc, r, c);
			}
			fillremain(r, c);
			fillremaincol(r, c);
			fillremaincol2(r, c);
		}
		
		printf("Case #%d:\n", i);
		for (x = 0; x < r; x++) {
			for (y = 0; y < c; y++) {
				printf("%c", arr[x][y]);
			}
			printf("\n");
		}
	}

	return 0;
}