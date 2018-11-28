#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < (int) (n); i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define maximize(a, b) ((a)<(b)?(a)=(b),1:0)
#define minimize(a, b) ((a)>(b)?(a)=(b),1:0)

void input();
void solve(int cs);

int main(int argc, char* argv[]) {
    if (argc == 1) freopen("input.txt", "r", stdin);
    int tc;
    cin >> tc;
    int l = 1, r = tc;
    if (argc > 1) {
        freopen(argv[2], "w", stdout);
        int n = atoi(argv[1]), i = atoi(argv[2]);
        l = tc / n * i + 1;
        r = i+1<n ? tc/n*(i+1) : tc;
    }
    for (int cs = 1; cs <= tc; cs++) {
        input();
        if (cs >= l && cs <= r) solve(cs);
    }
    return 0;
}

long long n, k;

void input() {
    cin >> n >> k;
}

void output(long long ans) {
    cout << ans/2 << " " << (ans-1)/2 << endl;
}

void solve(int cs) {
    cout << "Case #" << cs << ": ";
    long long val[2], cnt[2];
    val[0] = n; val[1] = n;
    cnt[0] = 1; cnt[1] = 0;
    while (true) {
        if (k <= cnt[0]) {
            output(val[0]);
            break;
        }
        if (k <= cnt[0] + cnt[1]) {
            output(val[1]);
            break;
        }
        k -= cnt[0] + cnt[1];
        long long ma = val[0]/2, mi = (val[1] - 1)/2;
        long long ca = 0, ci = 0;
        REP(i, 2) {
            if (val[i] / 2 == ma) ca += cnt[i];
            else ci += cnt[i];
            if ((val[i]-1)/2 == ma) ca += cnt[i];
            else ci += cnt[i];
        }
        val[0] = ma; val[1] = mi;
        cnt[0] = ca; cnt[1] = ci;
    }
}

