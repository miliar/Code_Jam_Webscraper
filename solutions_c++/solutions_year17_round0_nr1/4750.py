#include <bits/stdc++.h>

using namespace std;

char arr[1010];
int t, k, ans;
bool f = true;

int main() {
	freopen ("inn","r",stdin);
	freopen ("myfile.txt","w",stdout);
	scanf("%d", &t);
	for (int kk = 1; kk <= t; kk++) {
		f = true;
		ans = 0;
		scanf(" %s%d", &arr, &k);
		int s = strlen(arr);
		for (int i = 0; i <= s - k; i++) {
			if (arr[i] == '-') {
				ans++;
				for (int j = i, c = 0; c < k; j++, c++) {
					if (arr[j] == '-') {
						arr[j] = '+';
					} else {
						arr[j] = '-';
					}
				}
			}
		}
		for (int i = 0; i < s; i++) {
			if (arr[i] == '-') {
				printf("Case #%d: IMPOSSIBLE\n", kk);
				f = false;
				break;
			}
		}
		if (f)
			printf("Case #%d: %d\n", kk, ans);
	}
	return 0;
}
