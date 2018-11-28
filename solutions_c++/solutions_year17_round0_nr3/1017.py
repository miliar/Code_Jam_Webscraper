#include <iostream>
using namespace std;

void solve(long long n, long long k)
{
    if (k == 1) {
        if (n & 1ll) {
            n /= 2;
            cout << n << ' ' << n << endl;
        }
        else {
            n /= 2;
            cout << n << ' ' << n-1 << endl;
        }
        return;
    }
    if (k & 1ll) solve((n-1)/2, (k-1)/2);
    else solve(n/2, k/2);
}

int main()
{
    int T;
    long long N, k;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> N >> k;
        printf("Case #%d: ", i);
        solve(N, k);
    }
    return 0;
}
