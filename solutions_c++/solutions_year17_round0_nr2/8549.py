#include <cstdio>
#include <string.h>

int Strlen(int n) {
	int a = 0;
	while (n != 0) {
		a++;
		n /= 10;
	}
	return a;
}

int Pow(int n, int k) {
	int sum = 1;
	for (int i = 0; i < k; i++) {
		sum *= n;
	}
	return sum;
}

int convert(char* N, int len) {
	int real_N = 0;
	for (int i = 0; i < len; i++) {
		real_N += (N[i] - '0') * Pow(10, len - i - 1);
	}
	return real_N;
}

bool zero_all(char *N, int len) {
	for (int i = 0; i < len; i++) {
		if (N[i] == '0') continue;
		else return false;
	}
	return true;
}

bool upper_check(char *N, int len) {
	int before_num = -1, flag = 0;

	for (int i = 0; i < len; i++) {
		int real_num = N[i] - '0';
		if (before_num <= real_num) {
			flag = 1; before_num = real_num;
		}
		else {
			return false;
		}
	}
	return true;
}

int go(char* N, int *len) {
	for (int k = 2; k <= *len; k++) {
		if (upper_check(N + *len - k, k)) {
			continue;
		}else{
			N[*len - k] -= 1;
			for (int i = *len - k + 1; i <= *len - 1; i++) {
				N[i] = '9';
			}
		}
	}
	return 0;
}
int main(void) {
	int T;
	char N[20];
	FILE* infp;
	FILE* oufp;
	infp = fopen("B-large.in", "r");
	oufp = fopen("output.ou", "w");

	fscanf(infp, "%d", &T);
	
	for (int i = 0; i < T; i++) {
		fscanf(infp, "%s", N);
		int len = strlen(N);
		int tmp = go(N, &len);
		int flag = 0;
		fprintf(oufp, "Case #%d: ", i + 1);
		for (int i = 0; i < len; i++) {
			if (N[i] == '0' && flag == 0) {
				continue;
			}
			flag = 1;
			fprintf(oufp,"%c", N[i]);
		 }
		fprintf(oufp,"\n");
	}
	fclose(infp); fclose(oufp);
}