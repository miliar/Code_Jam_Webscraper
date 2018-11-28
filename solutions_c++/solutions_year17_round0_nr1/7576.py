#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cstdio>
using namespace std;
const int MAX = 1100;
char buff[MAX];
bool arr[MAX];
int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        int k, n;
        scanf("%s%d", buff, &k);
        for(n = 0; buff[n]; ++n)
            arr[n] = buff[n] == '-';
        int lim = n - k + 1, cnt = 0;
        for(int i = 0; i < lim; ++i) {
            if(arr[i]) {
                ++cnt;
                for(int j = 0; j < k; ++j)
                    arr[i + j] ^= 1;
            }
        }
        bool flag = false;
        while(lim < n)
            flag |= arr[lim++];
        printf("Case #%d: ", t);
        if(flag)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", cnt);
    }
    return 0;
}
