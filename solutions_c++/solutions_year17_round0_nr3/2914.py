#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

typedef long long ll;

int main() {
    freopen("C-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    forn (q, t) {
        long long n, k;
        cin >> n >> k;
        cout << "Case #" << q + 1 << ": ";
        long long a = 1, b = 0;
        while (n) {
            if (k <= a) {
                long long x = n - 1;
                cout << (x / 2 + x % 2) << " " << (x / 2) << endl;
                break;
            }
            k -= a;
            if (k <= b) {
                long long x = n - 2;
                cout << (x / 2 + x % 2) << " " << (x / 2) << endl;
                break;
            }
            k -= b;
//            cerr << a << " " << n << "  " << b << " " << n - 1 << endl;
            long long na = 0, nb = 0;
            if (n % 2 == 0) {
                na += a;
                nb += a;
                nb += 2 * b;
            } else {
                na += b;
                nb += b;
                na += 2 * a;
            }
            a = na;
            b = nb;
            n /= 2;
        }
    }
    return 0;
}
