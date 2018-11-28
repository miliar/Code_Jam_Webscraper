#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int test;
ll k, res;

ll cal(ll k){
    if (k == 0)
        return 0;
    vector <int> digit;
    while (k){
        digit.push_back(k % 10);
        k /= 10;
    }
    reverse(digit.begin(), digit.end());

    ll res = 0;
    for (int i = 0; i < digit.size(); ++i){
        res = res * 10 + digit[i];
        if (i < digit.size() - 1 && digit[i] > digit[i + 1]){
            res = cal(res - 1);
            for (int j = i + 1; j < digit.size(); ++j)
                res = res * 10 + 9;
            break;
        }
    }

    return res;
}

int main(){
    //freopen("in.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &test);
    for (int tt = 1; tt <= test; ++tt){
        scanf("%lld", &k);
        res = cal(k);
        printf("Case #%d: %lld\n", tt, res);
    }
    return 0;
}


