#include <bits/stdc++.h>
#define fin(i, n) for (int i = 0; i < n; i++)
#define fin2(i, a, b) for (int i = a; i < b; i++)
#define ll long long

using namespace std;

int main() {
    int T;
    cin >> T;
    fin(I, T) {
        cout << "Case #" << I + 1 << ": ";
        ll n;
        cin >> n;
        ll v = 1;
        fin(i, 20) {
//            cerr << n << endl;
            if (((ll)(n / (10 * v))) % 10 > ((ll)(n / v)) % 10) n -= (n % (10 * v) + 1);
            v *= 10;
        }
        cout << n << endl;
    }
}
