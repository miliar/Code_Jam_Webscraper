#include <bits/stdc++.h>

using namespace std;

int T;
int k;
int lena;
char stra[5000];

void flip(int i) {
	if (i >= lena) {
		return;
	}
	if (stra[i] == '-') {
		stra[i] = '+';
	} else if (stra[i] == '+') {
		stra[i] = '-';
	}
}

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		memset(stra, 0, sizeof(stra));
		scanf("%s", stra);
		scanf("%d", &k);
		int ansa = 0;
		lena = strlen(stra);
		for (int i = 0; i <= lena - k; i++) {
			if (stra[i] == '-') {
				ansa++;
				for (int j = i; j < i + k; j++) {
					flip(j);
				}
			}
		}
		printf("Case #%d: ", t);
		for (int i = 0; i < lena; i++) {
			if (stra[i] == '-') {
				puts("IMPOSSIBLE");
				goto outa;
			}
		}
		printf("%d\n", ansa);
		outa: 0;
	}

	return 0;
}
