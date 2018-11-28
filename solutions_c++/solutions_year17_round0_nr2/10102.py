#include <cstdio>

int main(void) {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		long long int N, temp;
		int num[20], index = 0;
		bool found = false;
		scanf("%lld", &N);

		while (true) {
			temp = N;
			index = 0;
			while (temp > 0) {
				num[index] = temp % 10;
				temp = temp / 10;
				index++;
			}
			if (index == 1) {
				break;
			}
			else {
				bool next = false;
				for (int i = 0; i < index - 1; i++) {
					if (num[i] == 0 || num[i + 1] == 0 || num[i] < num[i + 1]) {
						next = true;
						break;
					}
				}
				if (next == false) {
					break;
				}
			}
			N--;
		}
		printf("Case #%d: %lld\n", i, N);
	}
	return 0;
}
