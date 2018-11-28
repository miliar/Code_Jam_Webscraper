#include <stdio.h>
#include <string.h>

void flipp(char *p) {
	*p = *p == '-' ? '+' : '-';
}

int count(int flip, char *line, int size) {
	int flips = 0;
	for (int i = 0; i <= size - flip; ++i) {
		if (line[i] == '-') {
			for (int j = i; j < i + flip; ++j) {
				flipp(line + j);
			}
			++flips;
		}
	}
	//for (int i = 1; i <= flip; ++i) {
	for (int i = 0; i < size; ++i) {
		//if (line[size - i] == '-') {
		if (line[i] == '-') {
			return -1;
		}
	}
	return flips;
}

void solve(int cas, char* line, int flip) {
	int result = count(flip, line, strlen(line));
	if (result >= 0) {
		printf("Case #%d: %d\n", cas, result);
	} else {
		printf("Case #%d: IMPOSSIBLE\n", cas);
	}
}

int main(int argc, char *argv[]) {
	int total;
	scanf("%d", &total);
	for (int i = 0; i < total; i++) {
		char line[1001] = { 0 };
		int flip;
		scanf("%s %d", line, &flip);
		solve(i + 1, line, flip);
	}
	return 0;
}