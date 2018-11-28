#include <bits/stdc++.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		std::string pancakes;
		std::cin >> pancakes;
		int K;
		scanf("%d", &K);
		int flips = 0;
		for (int i = 0; i < pancakes.length() - K + 1; i++) {
			if (pancakes[i] == '-') {
				for (int j = 0; j < K; j++) {
					if (pancakes[i + j] == '+')
						pancakes[i + j] = '-';
					else
						pancakes[i + j] = '+';
				}
				flips++;
			}
		}
		int flag = 0;
		for (int i = 0; i < pancakes.length(); i++) {
			if (pancakes[i] == '-') {
				flag = 1;
				break;
			}
		}
		if (flag)
			printf("Case #%d: %s\n", t + 1, "IMPOSSIBLE");
		else
			printf("Case #%d: %d\n", t + 1, flips);
	}
	return 0;
}