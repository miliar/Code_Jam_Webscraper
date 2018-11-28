#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int Times;
char lineEnd[15];

int main() {

    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    scanf("%d", &Times);
    gets(lineEnd);
    for (int times = 1; times <= Times; ++times) {
        printf("Case #%d: ", times);
		
		int r, c;
		scanf("%d%d", &r, &c);
	    gets(lineEnd);
	    printf("\n");
	    
	    char ans[r][c];
	    int row = -1;
		for (int i = 0; i < r; ++i) {
			gets(ans[i]);
			if (row >= 0) continue;
			for (int j = 0; j < c; ++j) {
				if (ans[i][j] != '?') {
					row = i;
					break;
				}
			}
		}
		
		for (int i = row; i < r; ++i) {
			char ch = '?';
			char cc = '?';
			for (int j = 0; j < c; ++j) {
				if (ans[i][j] == '?') {
					ans[i][j] = ch;
				} else {
					if (ch == '?') cc = ans[i][j];
					ch = ans[i][j];
				}
			}
			
			if (ch == '?') {
				for (int j = 0; j < c; ++j) {
					ans[i][j] = ans[i-1][j];
				}
			} else {
				for (int j = 0; j < c; ++j) {
					if (ans[i][j] == '?') {
						ans[i][j] = cc;
					} else {
						break;
					}
				}
			}	
		}
		
		for (int i = 0; i < row; ++i) {
			for (int j = 0; j < c; ++j)	{
				ans[i][j] = ans[row][j];
			}
		}
		
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) printf("%c", ans[i][j]);
			printf("\n");
		}
    }
	
    return 0;
}
