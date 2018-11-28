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

long long n;

void input() {
    cin >> n;
}

bool isTidy(long long a) {
    if (a <= 0) return false;
    int last = 9;
    while (a) {
        int d = a % 10;
        if (d > last) return false;
        last = d;
        a /= 10;
    }
    return true;
}

void solve(int cs) {
    cout << "Case #" << cs << ": ";
    long long p = 1;
    if (isTidy(n)) cout << n << endl;
    else {
        REP(i, 18) {
            if (isTidy(n/p*p - 1)) {
                cout << n/p*p-1 << endl;
                break;
            }
            p *= 10;
        }
    }
}

