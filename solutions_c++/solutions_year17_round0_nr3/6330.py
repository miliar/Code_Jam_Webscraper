#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include<time.h>
#include <iostream>
#include <queue> 

using namespace std;

#define MSIZE 1000001
int gapc[MSIZE];

/*int findgap(int n, int k)
{
	queue<int> q;
	int maxgap = n;

	q.push(n);

	while (k) {

		if (q.size() == 0)
			return 0;

		n = q.front();
		q.pop();

		if (n % 2 == 0) {
			if (n / 2 > 0) {
				q.push(n / 2);
				q.push(n / 2 - 1);
			}
		}
		else {
			if (n / 2 > 0) {
				q.push(n / 2);
				q.push(n / 2);
			}
		}

		k--;
		maxgap = q.front();
	}

	return maxgap;
}*/

int findgap(int n, int k)
{
	gapc[n]++;
	int m = n;

	while (k) {

		gapc[m]--;
	
		if (m % 2 == 0) {
			gapc[m / 2]++;
			gapc[m / 2 - 1]++;
		}
		else {
			gapc[m / 2] += 2;
		}  

		if (gapc[m] == 0) {
			
			while (gapc[m] == 0) {
				m--;
				if (m == 0)
					return 0;
			}
			//m = n;
		}
		k--;
	}

	return m;
}
int retmax(int a, int b) {
	if (a > b)
		return a;
	else
		return b;
}

int retmin(int a, int b) {
	if (a > b)
		return b;
	else
		return a;
}


int main()
{
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);

	int t, n, i, k, ls, rs;
	
	scanf("%d", &t);

	for (i = 1; i <= t; i++) {

		scanf("%d%d", &n, &k);

		memset(gapc, 0, sizeof(int) * MSIZE);

		int gap = findgap(n, k-1);

		if (gap == 0) {
			printf("Case #%d: %d %d\n", i, 0, 0);
			continue;
		}

		if (gap % 2 == 0) {
			ls = gap / 2 - 1;
			rs = gap / 2;
		}
		else {
			ls = rs = gap / 2;
		}
		printf("Case #%d: %d %d\n",i, retmax(ls, rs), retmin(ls, rs));
	}

	return 0;
}