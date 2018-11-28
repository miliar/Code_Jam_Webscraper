#include <bits/stdc++.h>

#define LL long long
#define PI 3.141592653589793238462643383279502384197

using namespace std;

const int maxn = 105;

int sc[maxn], ec[maxn], sj[maxn], ej[maxn], ac, aj, tt[2000], ct[2000];

bool isCover1(){
    for (int i = 0; i < 1440; i++){
        memset(ct, 0, sizeof(ct));
        for (int j = 0; j < 720; j++){
            int temp = i + j;
            if (temp >= 1440) temp -= 1440;
            ct[temp] = 1;
        }
        int flag = 1;
        for (int j = 0; j < 1440; j++)
            if (ct[j] == 0 && tt[j] == 1) flag = 0;
        if (flag) return true;
    }
    return false;
}

bool isCover2(){
    for (int i = 0; i < 1440; i++){
        memset(ct, 0, sizeof(ct));
        for (int j = 0; j < 720; j++){
            int temp = i + j;
            if (temp >= 1440) temp -= 1440;
            ct[temp] = 1;
        }
        int flag = 1;
        for (int j = 0; j < 1440; j++)
            if (ct[j] == 0 && tt[j] == 2) flag = 0;
        if (flag) return true;
    }
    return false;
}

int main(){
    //freopen("B-small-attempt2.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++){
        scanf("%d%d", &ac, &aj);
        memset(tt, 0, sizeof(tt));
        for (int i = 1; i <= ac; i++){
            scanf("%d%d", &sc[i], &ec[i]);
            sc[i] %= 1440;
            ec[i] %= 1440;
            if (sc[i] > ec[i])
                ec[i] += 1440;
            for (int j = sc[i]; j < ec[i]; j++)
                tt[j % 1440] = 1;
        }
        for (int i = 1; i <= aj; i++){
            scanf("%d%d", &sj[i], &ej[i]);
            sj[i] %= 1440;
            ej[i] %= 1440;
            if (sj[i] > ej[i])
                ej[i] += 1440;
            for (int j = sj[i]; j < ej[i]; j++)
                tt[j % 1440] = 2;
        }
        int ans = 2;
        if (ac + aj == 1)
            ans = 2;
        else{
            if (ac == 1 && aj == 1)
                ans = 2;
            else{
                if (ac == 2){
                    if (isCover1()) ans = 2; else ans = 4;
                }
                if (aj == 2){
                    if (isCover2()) ans = 2; else ans = 4;
                }
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
