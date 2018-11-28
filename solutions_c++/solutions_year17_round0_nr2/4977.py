#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <utility>

#define fi first
#define se second
#define mp make_pair
#define PI 3.14159265
#define INF 1023123123
#define REP(a, b) for (int a = 0; a < b; ++a)
#define FORU(a, b, c) for (int a = b; a <= c; ++a)
#define FORD(a, b, c) for (int a = b; a >= c; --a)

using namespace std;

int main() {
	int T;
	char number[22];

	scanf("%d", &T);

	FORU(tc, 1, T) {
		scanf("%s", number);

		int len = strlen(number);
		int pos;
		bool tidy = false;

		while (!tidy) {
			tidy = true;
			pos = 1;

			while ((pos < len) && tidy) {
				if (number[pos - 1] > number[pos]) {
					tidy = false;
				}
				else {
					++pos;
				}
			}

			if (!tidy) {
				while (pos > 0) {
					if (number[pos - 1] > number[pos]) {
						for (int i = pos; i < len; ++i)
							number[i] = '9';

						number[pos - 1] = number[pos - 1] - 1;
					}

					--pos;
				}
			}
		}

		printf("Case #%d: ", tc);

		pos = 0;
		bool print = false;

		while (pos < len) {
			if (print)
				printf("%c", number[pos]);
			else if (number[pos] != '0') {
				printf("%c", number[pos]);
				print = true;
			}

			++pos;
		}

		printf("\n");
	}

	return 0;
}