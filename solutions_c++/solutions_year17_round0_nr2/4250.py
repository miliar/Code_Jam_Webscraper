#include <cstdio>
#include <cstring>
int main() {
	int n;
	char str[30];
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		scanf("%s", str);
		int cur = 0;
		int len = strlen(str);
		while(cur+1 < len && str[cur] <= str[cur+1]) cur++;
		long long int ans = 0;
		if(cur+1 != len) {
			while(cur > 0 && str[cur] == str[cur-1]) cur--;
			for(int j = cur+1; j < len; j++) str[j] = '0';
			sscanf(str, "%lld", &ans);
			ans--;
		}
		else sscanf(str, "%lld", &ans);
		printf("Case #%d: %lld\n", i+1, ans);
	}
	return 0;
}
