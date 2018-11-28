//Every cloud has a silver lining
//Hakuna matata

#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;

#define pb push_back
#define fi first
#define se second
#define sqr(x) ((x) * (x))

const char* fin = "1c17_c.inp";
const char* fon = "1c17_c.out";

#define oo (int) (1e9+7)
#define maxn (int) (105)

double a[maxn];
int n, k;
double U;

void sol() {
    sort(a + 1, a + n + 1);
    double lo = 0, hi = 1, mid;
    for(int j = 1; j <= 1000; ++j) {
        mid = (lo + hi) / 2;
        double tmp = U;
        bool isOk = true;
        for(int i = 1; i <= n; ++i) {
            if (mid < a[i]) break;
            if (mid > a[i]) {
                tmp -= (mid - a[i]);
                if (tmp < 0) {
                    isOk = false;
                    break;
                }
            }
        }
        if (isOk) lo = mid; else hi = mid;
    }

    double res = 1;

    for(int i = 1; i <= n; ++i) {
        if (a[i] < mid) a[i] = mid;
        res *= a[i];
    }

    cout << fixed;
    cout << setprecision(9) << res;
}

void inp() {
    int t;
    cin >> t;
    for(int iT = 1; iT <= t; ++iT) {
        cout << "Case #" << iT << ": ";

        cin >> n >> k;
        cin >> U;
        for(int i = 1; i <= n; ++i) cin >> a[i];
        sol();

        cout << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    freopen(fin, "r", stdin);freopen(fon, "w", stdout);
    inp();
    return 0;
}
