#include <bits/stdc++.h>

#define maxn 100000008
#define pp push_back
#define pf push_front
#define mp make_pair
#define fs first
#define sc second

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

char a[50][50];

int main(int argc, char *argv[])
{
	/* freopen("in", "r", stdin); */
	/* freopen("out", "w", stdout); */
	
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		int r, c;
		scanf("%d %d", &r, &c);
		for (int i = 1; i <= r; ++i) {
			for (int j = 1; j <= c; ++j) {
				scanf(" %c", &a[i][j]);
			}
		}

		for (int i = 1; i <= r; ++i) {
			int x = -1;
			char y = '.';
			for (int j = 1; j <= c; ++j) {
				if(a[i][j] == '?'){
					if(x == -1){
						x = j;
					}
				}else{
					if(x != -1){
						for (int k = x; k < j; ++k) {
							a[i][k] = a[i][j];
						}
					}
					y = a[i][j];
					x = -1;
				}
			}
			if(x != -1 && y != '.'){
				for (int j = x; j <= c; ++j) {
					a[i][j] = y;
				}
			}
		}

		for (int i = 1; i <= r; ++i) {
			if(a[i][1] == '?'){
				if(i > 1){
					for (int j = i-1; j >= 1; ++j) {
						if(a[j][1] != '?'){
							for (int k = j + 1; k <= i; ++k) {
								for (int l = 1; l <= c; ++l) {
									a[k][l] = a[j][l];
								}
							}
							break;
						}
					}
				}else{
					for (int j = i + 1; j <= r; ++j) {
						if(a[j][1] != '?'){
							for (int k = i; k < j; ++k) {
								for (int l = 1; l <= c; ++l) {
									a[k][l] = a[j][l];
								}
							}
							break;
						}
					}
				}
			}
		}

		printf("Case #%d:\n", tc);
		for (int i = 1; i <= r; ++i) {
			for (int j = 1; j <= c; ++j) {
				printf("%c", a[i][j]);
			}
			printf("\n");
		}

	}
	return 0;
}
