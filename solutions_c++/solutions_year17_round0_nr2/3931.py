#include<cstdio>

int main() {
	int t;
	scanf("%d", &t);

	for (int case_ = 1; case_ <= t; case_++) {
		char n[20];
		scanf("%s\n", n);
		int i = 0;
		printf("1 - %s\n", n);

		while (n[i+1] && n[i] <= n[i+1])
			i++;
		if (n[i+1]) {
			do {
				printf("1 - %s\n", n);
				n[i]--;
				i--;
			} while (i >= 0 && n[i+1]<n[i]);

			i+=2;
			while (n[i])
				n[i++] = '9';
		}
		char* np = n;
		while (*np == '0')
			np++;
		printf("Case #%d: %s\n", case_, np);
	}
}
