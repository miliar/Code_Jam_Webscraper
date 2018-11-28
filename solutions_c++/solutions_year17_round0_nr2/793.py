#include <bits/stdc++.h>

using namespace std;

long long p[10001];
char str[1001];
int tp = 0;

bool check(int id) {
	for (int i = 1; i <= id; i ++)
		if (str[i - 1] > str[i]) return false;
	return true;
} 
int main( ) {
	int T;
	scanf("%d", &T);
	while (T --) {
		scanf("%s", str + 1);
		int n = (int )(strlen(str + 1));
		str[0] = '0';
		p[n] = 1;
		long long x = 0;
		for (int i = n - 1; i >= 1; i --) p[i] = p[i + 1] * 10;
		for (int i = 2; i <= n + 1; i ++) {
			if (str[i - 1] == '0') continue;
			if (i != n + 1) str[i - 1] --;
			if (check(i - 1)) {
				if (i != n + 1) str[i - 1] ++;
				long long y = 0;
				for (int j = 1; j <= i - 1; j ++)
					y += p[j] * (str[j] - '0');
				if (i != n + 1) y --;
				x = max(x, y);
			}
			else {
				if (i != n + 1) str[i - 1] ++;
			}
		} 
		printf("Case #%d: ", ++ tp);
		cout << x << endl;
	}
	return 0;
}
				
