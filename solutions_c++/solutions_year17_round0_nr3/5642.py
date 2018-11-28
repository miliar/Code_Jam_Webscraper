#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef pair<int, int> ii;

#define pb push_back
#define fi first
#define se second
#define sqr(x) ((x) * (x))

const char* fin = "quali17c.inp";
const char* fon = "quali17c.out";

#define oo (int) (1e9+7)
#define maxn (int) (1e6+6)

bool emp[maxn];
int L[maxn], R[maxn];
int n, k;

void buff() {
    memset(emp, true, sizeof(emp));
    for(int person = 1; person <= k; ++person) {
        int Lm = 0, Rm = n + 1;
        for(int i = 1; i <= n; ++i) {
            L[i] = i - Lm - 1;
            if (!emp[i]) Lm = i;
        }
        for(int i = n; i >= 1; --i) {
            R[i] = Rm - i - 1;
            if (!emp[i]) Rm = i;
        }
        int pos = 0, mI = 0, mA = 0;
        for(int i = 1; i <= n; ++i) if (emp[i]) {
            int tmp_mI = min(L[i], R[i]);
            int tmp_mA = max(L[i], R[i]);
            if ((tmp_mI > mI) || (tmp_mI == mI && tmp_mA > mA)) {
                pos = i;
                mI = tmp_mI;
                mA = tmp_mA;
            }
        }
        emp[pos] = false;
        if (person == k) cout << mA << ' ' << mI;
    }
}

void inp() {
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        cin >> n >> k;
        if (n <= 1000) buff();
        cout << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    freopen(fin, "r", stdin);freopen(fon, "w", stdout);
    inp();
    return 0;
}
