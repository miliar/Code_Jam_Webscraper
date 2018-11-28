#pragma warning(disable:4996)
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

char a[26][26];

int main() {
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	int R,C;
	for (int tc = 1; tc <= T; tc++) {
		cin >> R;
		cin >> C;

		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				cin >> a[i][j];
			}
		}

		char c;
		int first = -1;
		for (int i=0; i<R; i++) {
			int j = 0;
			while (a[i][j] == '?') {
				j++;
			}
			if (j==C) {
				if (first != -1) {
					for (int k=0; k<C; k++) {
						a[i][k] = a[i-1][k];
					}
				}
			} else {
				if (first == -1) {
					first = i;
				}
				c = a[i][j];
				for (int k=0; k<j; k++) {
					a[i][k] = c;
				}
				for (int k=j+1; k<C; k++) {
					if (a[i][k] == '?') {
						a[i][k] = c;
					} else {
						c = a[i][k];
					}
				}
			}
		}

		for (int i=first-1; i>=0; i--) {
			for (int k=0; k<C; k++) {
				a[i][k] = a[i+1][k];
			}
		} 


		printf("Case #%d:\n", tc);
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				printf("%c", a[i][j]);
			}
			printf("\n");
		}
		
		

	}
	return 0;
}
