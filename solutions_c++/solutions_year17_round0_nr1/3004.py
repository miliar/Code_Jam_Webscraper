#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T;
char s[1010];
int main() {
    cin >> T;
    for (int C = 1, k; C <= T; C++) {
        scanf("%s%d", s, &k);
        int n = strlen(s), ans = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                if (i > n - k) {
                    ans = -1;
                    break;
                }
                for (int j = 0; j < k; j++) s[i+j] = (short)'+' + '-' - s[i+j];
                ans++;
            }
        }
        printf("Case #%d: ", C);
        if (ans == -1) puts("IMPOSSIBLE"); else cout << ans <<endl;
    }
}