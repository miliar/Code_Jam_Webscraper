#include <bits/stdc++.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		std::string num;
		std::cin >> num;
		int l = num.length();
		int flag = -1;
		for (int i = 1; i < l; i++) {
			if (num[i] < num[i - 1]) {
				flag = i;
				break;
			}
		}
		if (flag == -1) {
			printf("Case #%d: ", t + 1);
			std::cout << num << std::endl;
			continue;
		}
		for (int j = flag - 1; j >= 0; j--) {
			num[j]--;
			if (num[j] >= num[j - 1]) {
				flag = j;
				break;
			}
		}
		for (int j = flag + 1; j < l; j++)
			num[j] = '9';
		printf("Case #%d: ", t + 1);
		for (int j = 0; j < l; j++)
			if (num[j] != '0')
				printf("%c", num[j]);
		printf("\n");
	}
	return 0;
}