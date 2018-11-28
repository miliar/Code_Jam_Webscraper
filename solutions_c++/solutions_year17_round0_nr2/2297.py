#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int t;

void proc(int id) {
	char c;
	char str[1000];
	int n = 0, k;
	while ((c = getchar()) != '\n') {
		str[n] = c;
		n++;
	}

	int mark = n;

	for (int i = n-1; i > 0; i--)
		if (str[i] < str[i - 1]) {
			str[i] = '9';
			str[i - 1]--;
			mark = i;
		}

	printf("Case #%d: ", id);
	int i;
	for (i = 0; i < n; i++)
		if (str[i] >= '1')
			break;

	for (i = i; i < n; i++){
		if (i > mark)
			printf("9");
		else
		if (str[i] >= '0')
			printf("%c", str[i]);

	}
	printf("\n");
}

int main() {
	scanf("%d\n", &t);

	for (int i = 0; i < t; i++)
		proc(i + 1);

	return 0;
}
