#include <bits/stdc++.h>

using namespace std;
const int MAXN = 27;

void setmin (int &a, int b) {
	if (a > b) {
		a = b;
	}
}

void setmax (int &a, int b) {
	if (a < b) {
		a = b;
	}
}

int N, M;
char S[MAXN][MAXN];
bool isall[MAXN];

void go() {
	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; i++) {
		scanf("%s", S[i]);
		isall[i] = true;
		for (int j = 0; j < M; j++) {
			if (S[i][j] != '?') {
				isall[i] = false;
				break;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		if (!isall[i]) {
			//then copy it
			for (int j = 0; j < M; j++) {
				if (isalpha(S[i][j])) {
					for (int k = j - 1; k >= 0 && S[i][k] == '?'; k--) {
						S[i][k] = S[i][j];
					}
					for (int k = j + 1; k < M && S[i][k] == '?'; k++) {
						S[i][k] = S[i][j];
					}
				}
			}

			for (int r = i - 1; r >= 0 && isall[r]; r--) {
				memcpy(S[r], S[i], sizeof(S[i]));
			}
			for (int r = i + 1; r < N && isall[r]; r++) {
				memcpy(S[r], S[i], sizeof(S[i]));
			}
		}
	}

	for (int i = 0; i < N; i++) {
		puts(S[i]);
	}
}

int main() {
	int nq;
	scanf("%d", &nq);
	for (int i = 1; i <= nq; i++) {
		printf("Case #%d:\n", i);
		go();
	}
}
