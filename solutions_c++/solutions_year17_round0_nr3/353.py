#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

ll N, K;

map<ll, ll> dp;

map<ll, int> chk;
vector<ll> arr;

void dfs(ll n) {
    if(n == 0) return;
    if(chk[n]) return;
    arr.push_back(n);
    chk[n] = 1;
    if(n == 1) return;
    dfs((n - 1) / 2);
    dfs(n - 1 - (n - 1) / 2);
}

void main2(int tc) {
    scanf("%lld %lld", &N, &K);

    arr.clear();
    chk.clear();
    dp.clear();

    dfs(N);
    sort(arr.begin(), arr.end());

    dp[N] = 1;
    for(int i = arr.size() - 1; i >= 0; i--) {

        dp[ arr[i] - 1 - (arr[i] - 1) / 2 ] += dp[ arr[i] ];
        dp[ (arr[i] - 1) / 2 ] += dp[ arr[i] ];

    }
/*
    for(int i = 0; i < arr.size(); i++) {
        cout << arr[i] << ' ' << dp[ arr[i] ] << endl;
    }
//*/
    printf("Case #%d: ", tc);
    for(int i = arr.size() - 1; i >= 0; i--) {
        if(dp[ arr[i] ] >= K) {
            printf("%lld %lld\n", arr[i] - 1 - (arr[i] - 1) / 2, (arr[i] - 1) / 2);
            break;
        }
        K -= dp[ arr[i] ];
    }
}

int TC;
int main() {
    freopen("inputC.txt", "r", stdin);
    freopen("outputC.txt", "w", stdout);
    scanf("%d", &TC);
    for(int i = 1; i <= TC; i++) main2(i);
}
