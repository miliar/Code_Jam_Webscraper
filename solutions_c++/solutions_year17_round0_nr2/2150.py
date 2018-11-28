#include <cstring>
#include <iostream>
using namespace std;

int main() {
	int T;

	scanf("%d", &T);
	for (int caseN = 1; caseN <= T; caseN++) {
		char input[20];
		char ans[20];
		int startP = 0;

		scanf("%s", &input);
		memcpy(ans, input, sizeof(input));
		for (int i = 0; i < strlen(input) - 1; i++) {
			if (input[i] <= input[i + 1]) {
				ans[i] = input[i];
				if (input[i] < input[i + 1])
					startP = i + 1;
			} else {
				ans[startP] = input[startP] - 1;
				for (int j = startP + 1; j < strlen(input); j++)
					ans[j] = '9';
				break;
			}
		}

		printf("Case #%d: ", caseN);
		if (ans[0] == '0') printf("%s\n", ans + 1);
		else printf("%s\n", ans);
	}

	return 0;
}