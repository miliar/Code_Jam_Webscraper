#include <bits/stdc++.h>

using namespace std;

const int MAX_D = 20;
int T;
long long N;
int digits[MAX_D];
int dp[MAX_D];

int split(long long n) {
    int len = 0;
    while (n > 0LL) {
        digits[len++] = n % 10LL;
        n /= 10LL;
    }
    return len;
}

int main() {
    ifstream fin("B.in");
    ofstream fout("B.out");

    fin >> T;
    for (int t = 1; t <= T; t++) {
        fin >> N;
        fout << "Case #" << t << ": ";
        int length = split(N);

        dp[0] = digits[0];
        for (int i = 1; i < length; i++) {
            if (dp[i - 1] >= digits[i])
                dp[i] = digits[i];
            else dp[i] = digits[i] - 1;
        }

        long long ans = 0LL;
        for (int i = length - 1; i >= 0; i--) {
            ans = ans * 10LL + (long long)dp[i];
            if (dp[i] < digits[i])
                for (i--; i >= 0; i--)
                    ans = ans * 10LL + 9LL;
        }

        fout << ans << "\n";
    }

    fin.close();
    fout.close();

    return 0;
}
