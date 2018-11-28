#include <bits/stdc++.h>

#define MN 1001000
#define w1 while(1)
#define debug(a) cout << a << endl
#define pb push_back
#define mp make_pair

using namespace std;
typedef long long ll;

struct evento {
    int a1, a2, a3, rem;
    friend bool operator <(evento const& a, evento const& b) {
        return tie(a.a1, a.a2, a.a3, a.rem) < tie(b.a1, b.a2, b.a3, b.rem);
    }
};

map<evento, int> dp;

int n, T, p, a[110], freq[4], ans;
//char s[MN]; string str;


    //1 + 1 + 2
    //1 + 3
    //2 + 2
    //2 + 3 + 3
int solve(int a1, int a2, int a3, int rem) {
    evento p = {a1, a2, a3, rem};
    if(dp.find(p) != dp.end()) return dp[p];

    int x = 0;
    if(a1) x = max(x, solve(a1 - 1, a2, a3, (rem + 3) % 4) + (rem == 0));
    if(a2) x = max(x, solve(a1, a2 - 1, a3, (rem + 2) % 4) + (rem == 0));
    if(a3) x = max(x, solve(a1, a2, a3 - 1, (rem + 1) % 4) + (rem == 0));

    return dp[p] = x;
}

int solve() {
    int ret = 0;
    if(p == 2) {
        ret = int(ceil(freq[1] / 2.0) + 1e-6);
    }

    else if(p == 3) {
        ret = min(freq[1], freq[2]);
        freq[1] -= ret;
        freq[2] -= ret;

        ret += int(ceil(freq[1] / 3.0) + 1e-6);
        ret += int(ceil(freq[2] / 3.0) + 1e-6);
    }

    else {
        ret = solve(freq[1], freq[2], freq[3], 0);
    }

    ret += freq[0];
    return ret;
}

void clear_() {
    memset(freq, 0, sizeof freq);
    dp.clear();
}

int main() {
    freopen("A-largez.in", "r", stdin);
    freopen("A-largez.out", "w", stdout);

    scanf("%d", &T);
    for(int t=1; t<=T; t++) {
        clear_();
        scanf("%d %d", &n, &p);

        for(int i=0; i<n; i++) {
            scanf("%d",&a[i]);
            if(a[i] >= p) freq[a[i] % p]++;
            else freq[a[i]]++;
        }

        printf("Case #%d: %d\n", t, solve());
    }
    return 0;
}

