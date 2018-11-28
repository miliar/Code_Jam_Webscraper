#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check(char *number, int size) {
	for (int i = 1; i < size; ++i) {
		if (number[i - 1] > number[i]) {
			return 0;
		}
	}
	return 1;
}

long long decrease(char *number, int size) {
	while (!check(number, size)) {
		int b = 0;
		for (int i = 0; i < size; ++i) {
			if (number[i] > number[i + 1]) {
				--number[i];
				for (int j = i + 1; j < size; ++j)
				{
					number[j] = '9';
					b = 1;
				}
				if (b) {
					break;
				}
			}
		}
	}
	return atoll(number);
}

void solve(int cas, char* number) {
	printf("Case %d: %lld\n", cas, decrease(number, strlen(number)));
}

int main(int argc, char *argv[]) {
	int total;
	scanf("%d", &total);
	for (int i = 0; i < total; i++) {
		char number[128];
		scanf("%s", &number);
		solve(i + 1, number);
	}
	return 0;
}