#include <bits/stdc++.h>
using namespace std;

int TC;
char arr[1005], k;

int main() {
    scanf("%d", &TC);
    for (int zz = 1; zz <= TC; zz++) {
        scanf("%s %d", arr, &k);
        int len = strlen(arr);
        int ans = 0;

        for (int i = 0; i < len-k+1; i++) {
            if (arr[i] == '-') {
                ans++;
                for (int j = i; j < i+k; j++) {
                    if (arr[j] == '-')
                        arr[j] = '+';
                    else if (arr[j] == '+')
                        arr[j] = '-';
                }
            }
        }
        bool possible = true;
        for (int i = 0; i < len; i++)
            if (arr[i] == '-')
                possible = false;

        printf("Case #%d: ", zz);
        if (!possible) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
}