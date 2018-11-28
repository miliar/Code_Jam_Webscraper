#include<stdio.h>
FILE *fo, *fp;
int main() {
	fopen_s(&fo, "input.txt", "r");
	fopen_s(&fp, "output.txt", "w");
	int T, t;
	fscanf_s(fo, "%d", &T);
	long long int N, S;
	for (t = 1; t <= T; t++) {
		fscanf_s(fo, "%lld %lld", &N, &S);
		long long int now, sum,  ans1, ans2, par;
		now = 1;
		sum = 0;
		par = N;
		
		while (sum+now < S) {
			sum += now;
			now *= 2;
			par = (par - 1) / 2;
		}

		long long int rest = (N-sum) - ((N-sum) / now) * now;
		if (rest >= (S-sum)) {
			par++;
		}
		ans2 = (par - 1) / 2;
		ans1 = ans2;
		if ((par - 1) % 2 == 1) {
			ans1++;
		}
		fprintf_s(fp, "Case #%d: %lld %lld\n", t, ans1, ans2);
	}
	return 0;
}