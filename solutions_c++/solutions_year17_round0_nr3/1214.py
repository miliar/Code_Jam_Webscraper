#include <stdio.h>

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");
  
int T;
long long N, K;

int main(void) {
	int i;
	long long cnt, sum;
	long long x1, x2;
	long long a1, a2;
	long long t1, t2;
	long long min, max, flag;
	int p;

	fscanf(in, "%d", &T);
	for (i = 1;i <= T;i ++) {
		fscanf(in, "%I64d %I64d", &N, &K);
		if (K == 1) {
			if (N%2 == 0) {
				max = N/2;
				min = N/2-1;
			} else {
				max = N/2;
				min = N/2;
			}
			a1 = a2 = -1;
		} else {
			cnt = 1; sum = 1;
			a1 = a2 = N;
			x1 = 1;
			x2 = 0;
		}

		flag = 0;
		while (a1 >= 0 && a2 >= 0) {
			t1 = x1; t2 = x2;
			if (a1%2 == 0) { // 큰수가 짝수면
				x1 = t1;
				x2 = t1;
				a1 = a1/2;
			} else {
				x1 = t1*2;
				x2 = 0;
				a1 = (a1-1)/2;
			}

			if (a2%2 == 0) { // 작은수가 짝수면
				x1 += t2;
				x2 += t2;
				a2 = (a2-1)/2;
			} else {
				x2 += t2*2;
				a2 = a2/2;
			}

			if (flag == 1) {
				if (p == 1 || p == 3) {
					max = a1;
					min = a2;
				} else if (p == 2) {
					max = min = a2;
				} else if (p == 4) {
					max = min = a1;
				}
				break;
			}
			
			cnt = cnt * 2;
			sum = sum + cnt;
			if (K <= sum) {
				flag = 1;
				if (K > sum-x2) { // 작은수라는
					if (a2%2 == 0) p = 1; // 짝수면
					else p = 2;
				} else { // 큰수라는
					if (a1%2 == 0) p = 3; // 짝수면
					else p = 4; // 홀수면
				}
			}
		}

		fprintf(out, "Case #%d: %I64d %I64d\n", i, max, min);
	}
	return 0;
}