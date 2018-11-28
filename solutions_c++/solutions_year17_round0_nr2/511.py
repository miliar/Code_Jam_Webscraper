#include <stdio.h>
#include <algorithm>

char str[21];
bool skipFirst;

void fix(int pos) {
	char c = str[pos];
	for (int i = pos; c != 0; i++, c = str[i]) {
		str[i] = '9';
	}
	pos--;
	str[pos]--;
	
	while (pos >= 1 && str[pos] < str[pos - 1]) {
		str[pos] = '9';
		str[pos - 1]--;
		pos--;
	}
	if (str[pos] <= '0') {
		str[pos] = 0;
		skipFirst = true;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	
	for (int t = 0; t < T; t++) {
		scanf("%s", str);
		skipFirst = false;

		char c = str[0];
		int biggest = 0;
		for (int i = 0; c != 0; i++, c = str[i]) {
			int next = c - '0';
			if (next < biggest) {
				fix(i);
				break;
			}
			else {
				biggest = std::max(biggest, next);
			}
		}
		
		if (skipFirst) {
			printf("Case #%d: %s\n", t + 1, &str[1]);
		}
		else {
			printf("Case #%d: %s\n", t + 1, str);
		}
	}

	return 0;
}
