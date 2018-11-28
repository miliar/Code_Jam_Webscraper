#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include<time.h>
#include <iostream>
#include <queue> 

using namespace std;

void reverse(char * arr, int j, int k) {

	for (int i = j; i < j + k; i++) {
		if (arr[i] == '-')
			arr[i] = '+';
		else
			arr[i] = '-';
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t, n, i, k, count, l, gi;
	char arr[1001];
	bool impossible = false;

	scanf("%d", &t);

	for (i = 1; i <= t; i++) {

		scanf("%s%d", arr, &k);
		
		count = 0;
		n = strlen(arr);
		impossible = false;

		for (int j = 0; j < n; j++) {
			if (arr[j] == '-') {
				if (n - j >= k) {
					reverse(arr, j, k);
					count++;
				}
				else
				{
					impossible = true;
					break;
				}
			}
		}

		if (!impossible)
			printf("Case #%d: %d\n", i, count);
		else
			printf("Case #%d: IMPOSSIBLE\n", i);
	}
	return 0;
}