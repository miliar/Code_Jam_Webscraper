#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define pb push_back
#define mp make_pair
#define iOS ios_base::sync_with_stdio(false)
#define L(x) (x << 1)
#define R(x) (x << 1) + 1
#define tt cout << '.' << '\n';

typedef long long ll;
typedef pair <ll, ll> pii;

//const int N = 1e2 + 20;

const int oo = 1e9 + 7;

int q, n;

bool N (int n) {
    int x = n % 10;
    while (n > 0) {
        int y = n % 10;
        if (y > x) return true;
        x = y;
        n /= 10;
    }
    return false;
}

int main() {
    iOS;
    cin >> q;
    for (int j = 0; j < q; ++j) {
        cout << "Case #" << j + 1 << ": ";
        cin >> n;
        while (N(n)) {
            n--;
        }
        cout << n << '\n';
    }
    return 0;
}
