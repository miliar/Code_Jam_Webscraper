#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

FILE *in = fopen("A-large.in", "r");
FILE *out = fopen("output.txt", "w");

int main() {

	int testcase, s;
	fscanf(in, "%d", &testcase);
	char arr[1005];
	for (int i = 0; i < testcase; i++) {
		int check = 0;
		memset(arr, NULL, sizeof(arr));
		fscanf(in, "%s %d", arr, &s);
		int j = 0, cnt = 0;
		int length = strlen(arr);
		for (int j = 0; j < length - s + 1; j++) {
			if (arr[j] == '-') {
				cnt++;
				for (int ch = 0; ch < s; ch++)
					arr[j + ch] = '+' + '-' - arr[j + ch];
			}
		}
		int k = 0;
		while (arr[k] != NULL) {
			if (arr[k] == '-') {
				fprintf(out, "Case #%d: ", i + 1);
				fprintf(out, "IMPOSSIBLE\n");
				check = -1;
				break;
			}
			k++;
		}

		if (check != -1)
			fprintf(out, "Case #%d: %d\n", i + 1, cnt);


	}


	return 0;
}