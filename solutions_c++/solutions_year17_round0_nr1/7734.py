#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 1024;

int main() {
	int tests;
	int n, k;
	char cakes[MAXN];

	scanf("%d", &tests);

	for (int case_no = 1; case_no <= tests; ++case_no) {
		scanf("%s %d", cakes, &k);
		
		n = strlen(cakes);

		int pos = 0, answer = 0;
		
		while (pos < n) {

			// Finding a position with '-'
			while (cakes[pos] == '+' && pos < n) {
				pos++;
			}

			// Didn't find one, exiting
			if (pos == n) break;

			// Found a position with '-'

			// Can't flip here
			if (pos + k - 1 >= n) {
				break;
			}

			// Make a flip
			for (int i = pos; i < pos + k; ++i) {
				if (cakes[i] == '+') cakes[i] = '-';
				else cakes[i] = '+';
			}

			answer++;
		}

		if (pos == n) { 
			printf("Case #%d: %d\n", case_no, answer);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", case_no);
		}
	}

	return 0;
}