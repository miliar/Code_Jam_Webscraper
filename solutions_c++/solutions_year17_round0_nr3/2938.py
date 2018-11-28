#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<ll> values;
ll target;

ll pos(ll a) {
    ll v = 1ll;
    while(2ll*v <= a) {
        v = 2ll*v;
    }
    return a-v;
}

void dfs(ll s1, ll q1, ll s2, ll q2, ll index, ll val) {
    s1--;
    s2--;
    ll mn = s1/2ll, mx = s2-s2/2ll;
    ll qmn, qmx;
    if (s1 % 2ll == 0) {
        qmn = 2ll*q1+q2;
        qmx = q2;
    }
    else {
        qmn = q1;
        qmx = 2ll*q2+q1;
    }
    if (index == target) {
        ll a, b;
        if (pos(index) < q2) {
            printf("%lld %lld\n", max(s2/2ll, s2-s2/2ll), min(s2/2ll, s2-s2/2ll));
        }
        else {
            printf("%lld %lld\n", max(s1/2ll, s1-s1/2ll), min(s1/2ll, s1-s1/2ll));
        }
        return;
    }
    if (2ll*index == values[val]) dfs(mn, qmn, mx, qmx, 2ll*index, val+1ll);
    else dfs(mn, qmn, mx, qmx, 2ll*index+1ll, val+1ll);
}

int main() {
    int t;
    scanf("%d", &t);
    for(int j=1;j<=t;j++) {
        long long n, k;
        scanf("%lld %lld", &n, &k);
        printf("Case #%d: ", j);
        vector<ll> temp;
        target = k;
        while(k) {
            temp.push_back(k);
            k = k/2ll;
        }
        for(int i=temp.size()-1; i>=0; i--) {
            values.push_back(temp[i]);
        }
        dfs(n, 1, n+1, 0, 1, 1);
        values.clear();
    }
    return 0;
}

