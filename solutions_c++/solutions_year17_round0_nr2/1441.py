#include <bits/stdc++.h>
#define err(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)

typedef long long ll;
using namespace std;

const int dd = (int)1001;

int A[21];

int main() {
    int t;
    cin >> t;

    for (int test = 1; test <= t; test++) {
        ll n, ans = 0;
        cin >> n;

        int ind = 0;
        while (n) {
            A[ind++] = n % 10;
            n /= 10;
        }

        reverse(A, A + ind);

        for (int i = ind - 1; i > 0; i--) {
            if (A[i - 1] > A[i]) {
                A[i - 1]--;
                for (int j = i; j < ind; j++) A[j] = 9;
            }
        }
        for (int i = 0; i < ind; i++) ans = ans * 10 + A[i];
        cout << "Case #" << test << ": " << ans << "\n";

    }
    return 0;
}

