#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define MOD
#define ADD(X,Y) ((X) = ((X) + (Y)%MOD) % MOD)
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;

int T;
int R, C;
char S[30][30];
bool empty[30];

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; ++i) {
			scanf("%s", S[i]);
		}
		for (int i = 0; i < R; ++i) {
			empty[i] = true;
			for (int j = 0; j < C; ++j) {
				if (S[i][j] != '?') empty[i] = false;
			}

			if (!empty[i]) {
				for (int j = 1; j < C; ++j) {
					if (S[i][j] == '?') S[i][j] = S[i][j - 1];
				}
				for (int j = C - 2; j >= 0; --j) {
					if (S[i][j] == '?') S[i][j] = S[i][j + 1];
				}
			}
		}
		for (int i = 1; i < R; ++i) if (empty[i] && !empty[i - 1]) {
			empty[i] = false;
			for (int j = 0; j < C; ++j) {
				S[i][j] = S[i - 1][j];
			}
		}
		for (int i = R - 2; i >= 0; --i) if (empty[i] && !empty[i + 1]) {
			empty[i] = false;
			for (int j = 0; j < C; ++j) {
				S[i][j] = S[i + 1][j];
			}
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < R; ++i) printf("%s\n", S[i]);
	}

	return 0;
}
