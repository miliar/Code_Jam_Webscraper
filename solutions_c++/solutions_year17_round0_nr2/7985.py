#include <iostream>
#include <cstdio>

using namespace std;

// 1324 -> 1299
// 110 -> 99
// 221 -> 199

char* tidy_numbers(char* str, int len) {
	int pos = 0;
	while ((pos < len-1) && (str[pos] <= str[pos+1])) {
		pos++;
	}
	if (pos == len-1) {
		return str;
	}
	for (int i=pos+1; i<len; i++) {
		str[i] = '9';
	}
	str[pos] = str[pos] - 1;
	while (pos > 0 && str[pos] < str[pos-1]) {
		str[pos] = '9';
		pos--;
		str[pos] = str[pos] - 1;
	}
	return str;
}

int main() {
	int tc;
	scanf("%d\n", &tc);
	char input[20];
	for (int i=1; i<=tc; i++) {
		scanf("%s\n", input);
		char* output = tidy_numbers(input, strlen(input));
		printf("Case #%d: %s\n", i, output[0] == '0' ? output + 1 : output);
	}
}