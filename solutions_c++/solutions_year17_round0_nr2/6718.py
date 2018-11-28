// Author: Wang, Yen-Jen
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const ll LIM = 1000000000000000000ll;

vector<ll> table;

void dfs(ll now) {
    if(now > LIM) return;
    table.push_back(now);
    int t = now % 10;
    for(int i = t; i <= 9; i++) dfs(now * 10 + i);
}

int main() {
    table.reserve(4000000);
    for(int i = 1; i <= 9; i++) dfs(i);
    sort(table.begin() , table.end());
    int T;
    cin >> T;
    for(int kcase = 1; kcase <= T; kcase++) {
        ll x;
        cin >> x;
        printf("Case #%d: %lld\n",kcase,table[(upper_bound(table.begin() , table.end() , x) - table.begin() - 1)]);
    }
    return 0;
}
