#include<cstdio>
#include<cstring>

bool has_flipped(char* p) {
	int i = 0;
	while (p[i]) {
		if (p[i] == '-')
			return true;
		i++;
	}
	return false;
}

void flip(char* p, int k) {
	for (int i = 0; i < k; i++) {
		if (p[i] == '-')
			p[i] = '+';
		else if (p[i] == '+')
			p[i] = '-';
	}
}

int main() {
	int t;
	scanf("%d", &t);

	for (int case_ = 1; case_ <= t; case_++) {
		char p[1001];
		int k;
		scanf("%s %d", p, &k);

		int c = 0;
		for (int i = 0; i + k <= strlen(p); i++) {
			if (p[i] == '-') {
				printf("%s\n",p);
				c += 1;
				flip(p+i, k);
			}
		}
		if (has_flipped(p))
			printf("Case #%d: IMPOSSIBLE\n", case_);
		else
			printf("Case #%d: %d\n", case_, c);
	}
	return 0;
}

