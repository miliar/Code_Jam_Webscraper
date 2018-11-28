#include <bits/stdc++.h>

using namespace std;

long long n, k;

void Solve() {
    long long N = n;
    map<long long, long long> count_;
    count_[N] = 1;
    while (true) {
        if (k > count_[N]) {
            k -= count_[N];
            if (N % 2 == 0) {
                count_[N/2-1] += count_[N];
                count_[N/2] += count_[N];
            }
            else {
                count_[N/2] += 2*count_[N];
            }
        }
        else {
            if (N % 2) cout << N / 2 << " " << N / 2;
            else cout << N / 2 << " " << N / 2 - 1;
            break;
        }

        if (k > count_[N-1]) {
            k -= count_[N-1];
            if ((N-1) % 2 == 0) {
                count_[(N-1)/2-1] += count_[N-1];
                count_[(N-1)/2] += count_[N-1];
            }
            else {
                count_[(N-1)/2] += 2*count_[N-1];
            }
        }
        else {
            if ((N-1) % 2) cout << (N-1) / 2 << " " << (N-1) / 2;
            else cout << (N-1) / 2 << " " << (N-1) / 2 - 1;
            break;
        }
        N /= 2;
    }
}

int test;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> test;
    for(int i = 1; i <= test; i++) {
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        Solve();
        if (i != test) cout << endl;
    }
}
