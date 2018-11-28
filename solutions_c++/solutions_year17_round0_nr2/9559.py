#include <stdio.h>

#define MAX_DIGIT 18

int main()
{
	int tCase;
	int i, k, flag;
	long long int n;
	long long int j;
	long long int result, temp;
	long long int m;

	scanf("%d", &tCase);

	for (i = 0; i < tCase; i++) {
		scanf("%lld", &n);
		for (j = n; j > 0; ) {
			flag = 1;
			temp = j;
			m = 10;
			for (k = 0; k < MAX_DIGIT; k++) {
				if (temp % 10 < ((temp / 10) % 10)) {
					flag = 0;
					break;
				}
				m *= 10;
				temp = temp / 10;
			}
			if (flag == 1) {
				result = j;
				break;
			}
			j = ((j / m)*m - 1);
		}
		printf("Case #%d: %lld\n", i + 1, result);
	}
	return 0;
}