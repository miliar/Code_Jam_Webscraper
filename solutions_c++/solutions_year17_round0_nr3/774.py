#include <iostream>
#include <string>

#define show(X) cout << #X << " = " << X << endl

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int tt=1; tt<=T; ++tt) {
        long long n, k;
        cin >> n >> k;

        int p = -1;
        for (long long temp=k; temp>0; temp/=2) p++;
        long long slice = (1LL)<<p;
        long long r_k = k - (slice - 1);
        long long n_n = n - (slice - 1);
        long long l_bound = n_n/slice;
        long long mod = n_n % slice;
        if (r_k <= mod)
            l_bound++;
        cout << "Case #" << tt << ": " << l_bound / 2 << " " << (l_bound - 1) / 2 << endl;
    }
    return 0;
}
