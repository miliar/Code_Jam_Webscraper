#include <bits/stdc++.h>

using namespace std;

#define FOR(i,n) for(int i = 0; i < n; ++i)
#define FOR1(i,n) for(int i = 1; i <= n; ++i)
#define FORK(i, k, n) for(int i = k; i < n; ++i)

char s[2000];
char m[2000];

int solve(char *s, int n, int k) {
    int res = 0;

    FOR(i, n - k + 1) {
        if(s[i] == '-') {
            FORK(j, i, i + k) {
                s[j] = (s[j] == '-') ? '+' : '-';
            }
            res++;
        }
    }

    bool ok = true;
    FOR(i, n) {
        if(s[i] == '-') {
            ok = false;
            break;
        }
    }

    if(!ok)
        return 10000000;
    else
        return res;
}

int main() {
    int t_;

    scanf("%d", &t_);

    FOR1(cas, t_) {
        int k;
        scanf("%s%d", s, &k);

        int n = strlen(s);

        strcpy(m, s);
        int ans = solve(m, n, k);
        strcpy(m, s);
        reverse(m, m + n);

        ans = min(ans, solve(m, n, k));

        if(ans != 10000000)
            cout<<"Case #"<<cas<<": "<<ans<<endl;
        else
            cout<<"Case #"<<cas<<": "<<"IMPOSSIBLE"<<endl;
    }

    return 0;
}
