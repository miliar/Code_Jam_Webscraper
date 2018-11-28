#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <string.h>
#include <stdlib.h>

using namespace std;

int r, c;
bool b[30];
char a[30][30];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("cakes.out", "w", stdout);
	int test; scanf("%d", &test);
	for(int t = 1; t <= test; t++) {
		printf("Case #%d:\n", t);
		scanf("%d%d\n", &r, &c);
		for(int i = 0; i <= r; i++) b[i] = 0;
		for(int i = 0; i < r; i++) {
			fgets(a[i], 29, stdin);
			for(int j = 0; j < c; j++) 
				if (a[i][j] != '?') b[i] = 1;
			if (b[i] == 0 && i > 0) {
				for(int j = 0; j < c; j++) a[i][j] = a[i - 1][j];
			}
			else if (b[i] == 1) {
				for(int j = 1; j < c; j++) 
					if (a[i][j - 1] != '?' && a[i][j] == '?')
						a[i][j] = a[i][j - 1];
				for(int j = c - 2; j >= 0; j--) 
					if (a[i][j] == '?' && a[i][j + 1] != '?')
						a[i][j] = a[i][j + 1]; 
			}
		}
		for(int i = r - 2; i >= 0; i--) {
			for(int j = 0; j < c; j++) 
				if (a[i][j] == '?') a[i][j] = a[i + 1][j];
		}
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) printf("%c", a[i][j]);
			printf("\n");
		}
	}
	fclose(stdin);
	fclose(stdout);
}