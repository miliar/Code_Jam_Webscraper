#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
#define MAX 1005

FILE *in = fopen("A-small-attempt0.in", "r");
FILE *out = fopen("output.txt", "w");
int T;
int K;
char str[MAX];
int min = -1;
int len;
void makeHappy(int now, int count) {

	int i;
	for (i = 0; i<len; i++) {
		if (str[i] == '-') break;
	}
	if (i == len){
		if (min == -1 || min>count) min = count;
		return;
	}

	if (now > len - K)
		return;

	for (i = now; i<now + K; i++){
		if (str[i] == '-') str[i] = '+';
		else str[i] = '-';
	}
	makeHappy(now + 1, count + 1);

	for (i = now; i<now + K; i++){
		if (str[i] == '-') str[i] = '+';
		else str[i] = '-';
	}
	makeHappy(now + 1, count);

}
int main()
{
	fscanf(in,"%d", &T);
	for (int a = 1; a <= T; a++){
		fscanf(in,"%s %d", str, &K);
		len = strlen(str);
		min = -1;
		makeHappy(0, 0);
		if (min == -1) {
			fprintf(out,"Case #%d: IMPOSSIBLE\n", a);
		}
		else {
			fprintf(out,"Case #%d: %d\n", a, min);
		}
	}

	return 0;
}