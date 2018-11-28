#include <cstdio>
#define uint64 unsigned long long 
using namespace std;
int get_length(uint64 x) {
	int length = 0;
	while (x) {
		x /= 10;
		length++;
	}
	return length;
}

uint64 pow(int base, int exp) {
	int i;
	uint64 ans = 1;
	for (i = 0; i<exp; i++)
		ans *= base;
	return ans;
}
int main()
{

	uint64 n;
	FILE *fw, *fr;
	int T, t, length, i, j;
	fr = fopen("B-large.in","r");
	fw = fopen("B-large.out","w");
	fscanf(fr, "%d", &T);
	for (t = 1; t <= T; t++) {
		int arr[20];
		for (i = 0; i<20; i++)arr[i] = -1;
		fscanf(fr, "%lld", &n);
		length = get_length(n);
		i = 0;
		while (n) {
			arr[i] = n % 10;
			n /= 10;
			i++;
		}
		int carry = -1;
		for (i = length - 1; i>0; i--) {

			if (i>0 && arr[i]<0) {
				arr[i] = 9;
			}
			if (arr[i] > arr[i - 1]) {
				arr[i - 1] = 9;
				arr[i]--;
				for (j = 0; j < i; j++)arr[j] = 9;
				i = length;
			}
		}
		fprintf(fw, "Case #%d: ", t);
		if (arr[length - 1] <= 0) i = length - 2;
		else i = length - 1;
		for (; i >= 0; i--)
			fprintf(fw, "%d", arr[i]);
		fprintf(fw, "\n");
	}
	fclose(fw);
	fclose(fr);
}