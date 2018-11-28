#include<stdio.h>
#define Min(a,b) (a < b ? a : b)
int len = 0;
int num[20];
char S[20];
int min;
void print() {
	bool Start = false;
	for (int i = 0; i < len; i++)
	{
		if (Start || num[i] != 0) {
			printf("%d", num[i]);
			Start = true;
		}
	}
	printf("\n");
}
void swap(int x) {
	num[x] = 9;
	if (x >= min)
		return;
	if (num[x - 1] == 0) {
		swap(x - 1);
	}
	else {
		num[x - 1]--;
	}
	return;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, test = 1;
	scanf("%d", &t);
	while (test <= t) {
		scanf("%s", S);
		len = 0;
		for (; S[len] != 0; len++)
			num[len] = S[len] - '0';
		min = len;
		printf("Case #%d: ", test++);
		if (len == 1) {
			print();
			continue;
		}
		bool end = false;
		while (!end) {
			end = true;
			for (int i = len - 1; i > 0; i--) {
				if (num[i] < num[i - 1]) {
					swap(i);
					min = Min(i, min);
					end = false;
				}
			}
		}
		print();
	}
}