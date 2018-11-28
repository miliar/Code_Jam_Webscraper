#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>

const int MAXN = 26;

char cake[MAXN][MAXN];

void split(int n, char *s) {
	char last;
	for (int i = 0; i < n; ++ i) {
		if (s[i] != '?') {
			last = s[i];
			break;
		}
	}

	for (int i = 0; i < n; ++ i) {
		if (s[i] != '?') {
			last = s[i];
		}
		else {
			s[i] = last;
		}
	}
}

int main() {
	int task;
	scanf("%d", &task);
	for (int task_index = 1; task_index <= task; ++ task_index) {
		int r, c;
		scanf("%d %d", &r, &c);
		int init = -1;
		for (int i = 0; i < r; ++ i) {
			scanf(" %s", cake[i]);
			for (int j = 0; j < c; ++ j) {
				if (init == -1 && cake[i][j] != '?') {
					init = i;
				}
			}
		}
		split(c, cake[init]);
		for (int i = 0; i < init; ++ i) {
			memcpy(cake[i], cake[init], c * sizeof(char));
		}

		for (int i = init + 1; i < r; ++ i) {
			bool has = false;
			for (int j = 0; j < c; ++ j) {
				if (cake[i][j] != '?') {
					has = true;
					break;
				}
			}
			if (has) {
				split(c, cake[i]);
			}
			else {
				memcpy(cake[i], cake[i - 1], c * sizeof(char));
			}
		}

		printf("Case #%d:\n", task_index);
		for (int i = 0; i < r; ++ i) {
			printf("%s\n", cake[i]);
		}
	}
	return 0;
}

