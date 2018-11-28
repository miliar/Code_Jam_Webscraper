#include <iostream>
#include <cstring>
using namespace std;

int flip(char c) {
	if (c == '-') {
		return '+';
	} else {
		return '-';
	}
}

int flip_cakes(char* target, int k) {
	int count = 0;
	int length = strlen(target);
	for (int i=0; i<length - k + 1; i++) {
		if (target[i] == '-') {
			for (int j=i; j<i+k; j++) {
				target[j] = flip(target[j]);
			}
			count++;
		}
	}
	for (int i=0; i<length; i++) {
		if (target[i] == '-') {
			return -1;
		}
	}
	return count;
}

int main() {
	int tc;
	scanf("%d\n", &tc);
	for (int i=1; i<=tc; i++) {
		char cake[1004];
		int k;
		scanf("%s %d\n", cake, &k);
		int result = flip_cakes(cake, k);
		if (result == -1) {
			printf("Case #%d: IMPOSSIBLE\n", i);
		} else {
			printf("Case #%d: %d\n", i, result);
		}
	}
}
