#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;

main() {
	freopen("B-large.in", "r", stdin);
	freopen("outBlarge.txt", "w", stdout);
	
	int t, tc = 1;
	scanf("%d", &t);
	char str[25];
	while(t--) {
		scanf("%s", str);
		int len = strlen(str);
		for(int i = 0; i < len - 1; i++) {
			if(str[i + 1] < str[i] && (i == 0 || str[i - 1] <= str[i] - 1)) {
				str[i]--;
				for(int j = i + 1; j < len; j++) {
					str[j] = '9';
				}
				break;
			} else if(str[i + 1] < str[i]){
				for(int j = i - 1; j >= 0; j--) {
					if(j == 0 || str[j - 1] <= str[j] - 1) {
						str[j]--;
						for(int k = j + 1; k < len; k++) {
							str[k] = '9';
						}
						break;
					}
				}
			}
		}
		long long ans = 0;
		sscanf(str, "%lld", &ans);
		printf("Case #%d: %lld\n", tc++, ans);
	}
}

