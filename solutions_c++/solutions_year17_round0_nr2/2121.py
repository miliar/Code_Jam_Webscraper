#include <cstdio>

using namespace std;


void proc(int caseno) {
	long long int num;
	scanf("%lld", &num);

	int digits[20];
	for (int i = 19; i >= 0; i--) {
		digits[i] = num % 10;
		num /= 10;
	}

	for (int i = 18; i >= 0; i--) {
		if (digits[i] > digits[i + 1]) {
			digits[i]--;
			for (int j = i + 1; j < 20; j++)
				digits[j] = 9;
		}
	}

	printf("Case #%d: ", caseno);
	int i;
	for (i = 0; i < 19 && digits[i] == 0; i++);
	for (; i < 20; i++)
		printf("%d", digits[i]);
	printf("\n");
}

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		proc(i + 1);
}




