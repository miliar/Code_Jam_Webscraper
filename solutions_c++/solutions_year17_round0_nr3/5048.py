#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("c-small-2.in","r",stdin);
    freopen("c-small-2.out","w",stdout);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cout << "Case #" << i+1 << ": ";

        long long n, k;
        cin >> n >> k;

        long long nlog = (long long) log2(n);
        long long klog = (long long) log2(k);

        if (klog == nlog) {
            cout << "0 0\n";
            continue;
        }

        long long num = pow(2, klog+1);
        long long sum = n - num + 1;
        long long quo = sum / num;
        long long rem = sum % num;

        if (rem > pow(2, klog)) {
            rem -= pow(2, klog);
            if (k - pow(2,klog) < rem) {
                cout << quo + 1 << " " << quo + 1 << "\n";
                continue;
            }
            cout << quo + 1 << " " << quo << "\n";
            continue;
        }

        if (k - pow(2, klog) < rem) {
            cout << quo + 1 << " " << quo << "\n";
            continue;
        }

        cout << quo << " " << quo << "\n";
    }
}
