#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int p;

map <pair<vector <int>, int>, int> dp;

int solve (pair<vector <int>, int> estado){

    if (dp.count(estado)) return dp[estado];
    auto &qtd = estado.first;
    auto &resto = estado.second;
    auto &ret = dp[estado];
    ret = 1<<30;
    if (qtd[0] + qtd[1] + qtd[2] + qtd[3] == 0) return ret = 0;

    for (int i = 0; i < p; i++){
        auto temp = qtd;
        if (!temp[i]) continue;
        temp[i]--;
        int r;
        if (resto >= i)
            r = resto - i;
        else{
            r = (p - (i - resto)) % p;
        }

        ret = min (ret, solve({temp, r}));
    }
    if (resto) ret++;

    return ret;
}

int main(){

    int tt;
    scanf ("%d", &tt);
    for (int cc = 1; cc <= tt; cc++){
        dp.clear();
        int n;
        scanf ("%d %d", &n, &p);
        int resto[4];

        memset(resto, 0, sizeof resto);

        for (int i = 0; i < n; i++){
            int a;
            scanf ("%d", &a);
            resto[a%p]++;
        }
        resto[0] = 0;
        int ans = n - solve({{resto[0], resto[1], resto[2], resto[3]}, 0});
        printf ("Case #%d: %d\n", cc, ans);
    }

    return 0;
}
