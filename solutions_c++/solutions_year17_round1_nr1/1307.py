#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

char grid[26][26];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int test = 1; test <= t; test++) {
		int r, c;
		scanf("%d %d", &r, &c);
		for(int i = 0; i<r; i++) {
			for(int j = 0; j<c; j++) {
				scanf(" %c", &grid[i][j]);
			}
		}
		for(int i = 0; i<r; i++) {
			for(int j = 0; j<c; j++) {
				if(grid[i][j] != '?') {
					for(int j_ = j-1; j_ >= 0; j_--) {
						if(grid[i][j_] != '?') break;
						grid[i][j_] = grid[i][j];
					}
					for(int j_ = j+1; j_ < c; j_++) {
						if(grid[i][j_] != '?') break;
						grid[i][j_] = grid[i][j];
					}
				}
			}
		}
		for(int i = 0; i<r; i++) {
			for(int j = 0; j<c; j++) {
				if(grid[i][j] != '?') {
					for(int i_ = i-1; i_ >= 0; i_--) {
						if(grid[i_][j] != '?') break;
						grid[i_][j] = grid[i][j];
					}
					for(int i_ = i+1; i_ < r; i_++) {
						if(grid[i_][j] != '?') break;
						grid[i_][j] = grid[i][j];
					}
				}
			}
		}
		printf("Case #%d:\n", test);
		for(int i = 0; i<r; i++) {
			for(int j = 0; j<c; j++) {
				printf("%c", grid[i][j]);
			}
			printf("\n");
		}
	}
	
	return 0;
}
