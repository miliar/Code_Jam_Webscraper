#include <cstdio>
#include <cstring>

int main() {
	char buf[1024];
	int T;
	int i, j, k;

	memset(buf, 0x00, sizeof(buf));
	fgets(buf, 1024, stdin);

	sscanf(buf, "%d", &T);

	for (i = 0; i < T; ++i) {
		memset(buf, 0x00, sizeof(buf));
		fgets(buf, 1024, stdin);

		char num[20];
		memset(num, 0x00, sizeof(num));
		sscanf(buf, "%s", num);

		int len = strlen(num);

		for (j = 0; j < len - 1; ++j) {
			if (num[j] > num[j + 1]) {
				break;
			}
		}

		if (j < len - 1) {
			for (k = j + 1; k < len; ++k) {
				num[k] = '9';
			}
			num[j] -= 1;

			while (j > 0 && num[j - 1] > num[j]) {
				num[j] = '9';
				num[j - 1] -= 1;
				--j;
			}
		}

		printf("Case #%d: ", i + 1);
		for (j = 0; j < len; ++j) {
			if (num[j] != '0')
				printf("%c", num[j]);
		}
		printf("\n");
	}

	return 0;
}