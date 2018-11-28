#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

long long n;
char s[100];

void read() {
	cin >> n;
}

void process() {
	int size = 0;
	while (n > 0) {
		s[size++] = n % 10;
		n /= 10;
	}
	reverse(s, s + size);
	int i = 0;
	while (i + 1 < size && s[i] <= s[i+1]) {
		i++;
	}
	if (i + 1 < size) {
		while (i > 0 && s[i-1] == s[i]) {
			i--;
		}
		s[i]--;
		for (int j = i + 1; j < size; j++) {
			s[j] = 9;
		}
	}
	long long res = 0;
	for (int j = 0; j < size; j++) {
		res = res * 10 + s[j];
	}
	cout << res << endl;
}

int main() {

	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}