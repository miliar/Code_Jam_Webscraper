#include <bits/stdc++.h>

#define LL long long

using namespace std;

LL num[2][2], cnt[2][2];

void Add(int idx, LL x, LL cx){
    if (cx == 0)
        return;
    //cout << x << ' ' << cx << endl;
    for (int i = 0; i < 2; i++){
        if (num[idx][i] == 0 || num[idx][i] == x){
            num[idx][i] = x;
            cnt[idx][i] += cx;
            break;
        }
    }
    return;
}

int main(){
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++){
        LL n, k, cur = 0, tag = 1;
        scanf("%I64d%I64d", &n, &k);
        memset(num, 0, sizeof(num));
        memset(cnt, 0, sizeof(cnt));
        num[tag][0] = n;
        cnt[tag][0] = 1;
        while(1){
           for (int i = 0; i < 2; i++){
                //cout << num[tag][i] << ' ' << cnt[tag][i] << endl;
                if (k <= cnt[tag][i]){
                    cur = num[tag][i];
                    break;
                }
                else{
                    k -= cnt[tag][i];
                }
           }
           if (cur > 0) break;
           //cout << endl;
           for (int i = 0; i < 2; i++){
                num[1 - tag][i] = 0;
                cnt[1 - tag][i] = 0;
           }
           for (int i = 0; i < 2; i++){
                //cout << num[tag][i] << endl;
                Add(1 - tag, num[tag][i] / 2, cnt[tag][i]);
                Add(1 - tag, (num[tag][i] - 1) / 2, cnt[tag][i]);
           }
           tag = 1 - tag;
        }
        printf("Case #%d: %I64d %I64d\n", cas, cur / 2, (cur - 1) / 2);
    }
    return 0;
}
