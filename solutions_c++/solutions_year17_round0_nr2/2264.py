#include <bits/stdc++.h>

using namespace std;

char str[1005];
int a[1005];
int n, k;

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T;
    scanf("%d", &T);
	for (int cas = 1; cas <= T; cas ++) {
        scanf("%s%d", str, &k);
        n = strlen(str);
        for(int i = 0; i < n; i ++) {
			a[i] = (str[i] == '+');
        }
        int cnt = 0;
        for(int i = 0; i < n; i ++) {
            if (a[i] != 1) {
                if(i + k > n) {
                    cnt = -1;
                    break;
                }
                cnt ++;
                for(int j = i; j < i + k; j ++) {
					a[j] ^= 1;
                }
            }
        }
        printf("Case #%d: ", cas);
        if(cnt == -1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", cnt);
		}
    }
    return 0;
}
