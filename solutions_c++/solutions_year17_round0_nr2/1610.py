#include <bits/stdc++.h>

#define LL long long

using namespace std;

const int maxn = 1005;

char num[25], te[25];

LL Solve(int p, int len){
    for (int i = 0; i < len; i++){
        te[i] = num[i];
    }
    te[p] -= 1;
    for (int i = p + 1; i < len; i++){
        te[i] = '9';
    }
    LL ans = 0;
    for (int i = 0; i < len; i++){
        if (i > 0 && te[i] < te[i - 1])
            return 0LL;
        ans = ans * 10LL + te[i] - '0';
    }
    return ans;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++){
        scanf("%s", num);
        int len = strlen(num);
        LL ans = 1LL, temp = 0LL;
        for (int i = 0; i < len; i++){
            if (i > 0 && num[i - 1] > num[i]){
                temp = 0LL;
                break;
            }
            temp = temp * 10LL + num[i] - '0';
        }
        if (temp > 0)
            ans = temp;
        else{
            for (int i = len - 1; i >= 0; i--){
                if (num[i] > '0'){
                    LL temp = Solve(i, len);
                    if (temp > ans)
                    ans = temp;
                }
            }
        }
        printf("Case #%d: %I64d\n", cas, ans);
    }
    return 0;
}
