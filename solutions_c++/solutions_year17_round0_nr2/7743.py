#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 32;

int main() {
	int tests;
	int n;
	char num[MAXN];

	scanf("%d", &tests);

	for (int case_no = 1; case_no <= tests; ++case_no) {
		scanf("%s", num);
		
		n = strlen(num);
		long long given = num[0] - '0';
		bool valid = true;
		long long answer = 0;

		for (int i = 1; i < n; ++i) {
			if (num[i] < num[i - 1]) valid = false;
			given = given * 10 + num[i] - '0';
		}
		
		if (valid) answer = given;

		for (int i = 0; i < n; ++i) {
			long long cur_num = 0;
			bool valid = true;

			for (int j = 0; j < i; ++j) {
				if (j > 0 && num[j] < num[j - 1]) valid = false;
				cur_num = cur_num * 10 + num[j] - '0';
			}
			
			if (!valid) continue;

			if (num[i] - 1 >= '0') {
				if (i > 0 && num[i - 1] > num[i] - 1) goto out;
				cur_num = cur_num * 10 + num[i] - 1 - '0';
				for (int j = i + 1; j < n; ++j) cur_num = cur_num * 10 + 9;
				if (cur_num <= given) {
					answer = max(answer, cur_num);
				}
			}
			out:;
		}

		printf("Case #%d: %lld\n", case_no, answer);
	}

	return 0;
}