#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

char pancake[10000];
int main()
{
    int T;cin>>T;
    for (int TT = 1; TT <= T; ++TT) {
        printf("Case #%d: ", TT);
        int k = 0;
        cin >> pancake >> k;
        int ans = 0;
        int len = strlen(pancake);
        for (int i = 0; i + k - 1 < len; ++i) {
            if(pancake[i] == '-') {
                ans ++;
                for (int j = i; j < i + k; ++j) {
                    if(pancake[j] == '-') pancake[j] = '+';
                    else pancake[j] = '-';
                }
            }
            // printf("%s\n", pancake);
        }
        bool flag = true;
        for (int i = len - k + 1; i < len; ++i) {
            if(pancake[i] == '-') flag = false;
        }
        if(flag) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}