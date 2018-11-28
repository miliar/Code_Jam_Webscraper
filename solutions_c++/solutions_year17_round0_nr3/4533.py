#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long long n, k;
        cin >> n >> k;
        long long p = floor(log2(k));
        long long div = 1;
        for (int i = 0; i < p; i++) {
            div *= 2;
        }
        long long left = (n - k + 1);
        long long pans = left / div + (left % div ? 1 : 0);
        cout << "Case #" << t << ": " << pans / 2 << " " << (pans - 1) / 2 << endl;
    }
}
