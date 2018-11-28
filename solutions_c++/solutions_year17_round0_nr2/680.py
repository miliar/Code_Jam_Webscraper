#include <bits/stdc++.h>
using namespace std;

char st[30];
int n;
int f[30];

bool ok() {
	for (int i = 0; i < n - 1; i++) {
		if (f[i] > f[i + 1]) {
			return false;
		}
	}
	return true;
}

void make() {
	int pos = 0;
	for (int i = 0; i < n - 1; i++) {
		if (f[i] > f[i + 1]) {
			pos = i;
			break;
		}
	}
	f[pos]--;
	for (int i = pos + 1; i < n; i++) {
		f[i] = 9;
	}
}

void work() {
	if (n == 0) {
		puts(st);
		return;
	}

	for (int i = 0; i < n; i++) {
		f[i] = st[i] - '0';
	}

	while (!ok()) {
		make();
	}

	int a = 0;
	while (a < n && f[a] == 0) {
		a++;
	}
	for (int i = a; i < n; i++) {
		printf("%d", f[i]);
	}
	puts("");
}

int main()
{
	int t;
	scanf("%d", &t);
	int case_num = 0;
	while (t--)
	{
		case_num++;
		printf("Case #%d: ", case_num);
		scanf("%s", st);
		n = strlen(st);
		work();
	}
	return 0;
}
