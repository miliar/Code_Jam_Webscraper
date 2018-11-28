#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;
int main() {
	int t;
	int tt = 0;
	FILE* fp;
	FILE* fp2;
	fp2 = fopen("B-large.in", "r");
	fp = fopen("output.out", "w");
	fscanf(fp2,"%d", &t);
	//scanf("%d", &t);
	while (t--) {
		tt++;
		char arr[20] = { 0 };
		fscanf(fp2,"%s", arr);
		//scanf("%s", arr);
		int len = strlen(arr);
		arr[len] = '9';
		char ans[20] = { 0 };
		for (int i = 0; i < len; i++) {
			if (arr[i] <= arr[i + 1])
				ans[i] = arr[i];
			else {
				int maxi = i;
				for (int j = i - 1; j >= 0; j--) {
					if (arr[j] == arr[i])
						maxi = j;
					else
						break;
				}
				ans[maxi] = arr[maxi] - 1;
				for (int j = maxi + 1; j < len; j++)
					ans[j] = '9';
				break;
			}
		}
		if (ans[0] == '0')
			fprintf(fp, "Case #%d: %s\n",tt, ans + 1);
		else
			fprintf(fp, "Case #%d: %s\n",tt, ans);
	}
}