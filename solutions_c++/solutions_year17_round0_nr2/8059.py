#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include<time.h>

void getdigits(int * arr, int n)
{
	int r, m, i;
	m = n;
	i = 2;

	while (m) {
		r = m % 10;
		m = m / 10;
		arr[i--] = r;
	}
}

bool findans(int * arr)
{
	if (arr[0] <= arr[1] && arr[1] <= arr[2])
		return true;
	else
		return false;
}

int formnum(int * arr)
{
	return 100 * arr[0] + 10*arr[1] + arr[2];
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

	int t, n, i, j;
	int digits[3];
	scanf("%d", &t);

	for (i = 1; i <= t; i++) {

		scanf("%d", &n);

		if (n < 10) {
			printf("Case #%d: %d\n", i, n);
			continue;
		}

		if (n == 1000) {
			printf("Case #%d: %d\n", i, 999);
			continue;
		}

		digits[0] = 0;
		digits[1] = 0;
		digits[2] = 0;
		getdigits(digits, n);

		while (findans(digits) == false) {
			if (digits[2] > 0)
				digits[2]--;
			else if (digits[2] == 0) {
				digits[2] = 9;
				if (digits[1] > 0)
					digits[1]--;
				else if (digits[1] == 0) {
					digits[1] = 9;
					if (digits[0] > 0)
						digits[0]--;
				}
			}
		}
		printf("Case #%d: %d\n",i, formnum(digits));
	}

	return 0;
}