#include <bits/stdc++.h>

using namespace std;

const int maxn = 20;

char str[maxn];
int a[maxn], n;

long long dfs(int m, bool f, long long res) {
	if(m == n) 	return res;
	if(f) {
		for(int i = m;i < n;++ i) {
			res = res*10+9;
		}
		return res;
	}
	long long ans;
	if(a[m] >= res%10) {
		if((ans = dfs(m+1, false, res*10+a[m])) == -1) {
			for(int i = a[m]-1;i >= res%10;-- i) if((ans = dfs(m+1, true, res*10+i)) != -1) {
				return ans;
			}
			return -1;
		} 
		return ans;
	}
	return -1;
}

int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int T, tCase = 0;	scanf("%d", &T);
	while(T --) {
		scanf("%s", str);
		printf("Case #%d: ", ++tCase);
		n = strlen(str);
		bool flag = false;
		for(int i = 0;i < n;++ i) if(flag || str[i] != '0') {
			flag = true;
			a[i] = str[i]-'0'; 
		}
		long long ans = dfs(0, false, 0);
		printf("%I64d\n", ans);
	}
	return 0;
}