#include <bits/stdc++.h>

using namespace std;

int main() {
	int i, n, j;
	bool arr[1001];
	for (i = 0; i < 1001; i++)
		arr[i] = (i % 10) && (i < 10 || (i / 10) % 10) && (i < 100 || (i / 100) % 10) && (i % 10) >= (i / 10) % 10 && (i / 10) % 10 >= (i / 100) % 10;
	cin >> n;
	for (i = 1; i <= n; i++) {
		cin >> j;
		for (j++; !arr[--j];);
		printf("Case #%d: %d\n", i, j);
	}
}