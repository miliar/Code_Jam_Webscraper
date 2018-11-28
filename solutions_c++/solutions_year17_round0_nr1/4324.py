#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main(){
    int t;
    scanf("%d", &t);
    for (int z = 1; z <= t; z++){
        char s[1000];
        bool f[1000];
        int k;
        scanf("%s %d", s, &k);
        for (int i = 0; i < strlen(s); i++)
            if (s[i] == '+') f[i] = true;
            else f[i] = false;
        int ans = 0;
        for (int i = 0; i < strlen(s) - k + 1; i++){
            if (!f[i]){
                ans = ans + 1;
                for (int j = 0; j < k; j++)
                    f[i + j] = !f[i + j];
            }
        }
        bool flag = true;
        for (int i = strlen(s) - k + 1; i < strlen(s); i++)
            flag = flag && f[i];
        printf("Case #%d: ", z);
        if (flag) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}