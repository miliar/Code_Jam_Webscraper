#include <bits/stdc++.h>

using namespace std;

long long exponent(long long a, long long b) {
    long long ret = 1;
    for (long long i = 0; i < b; i++) {
        ret *= a;
    }
    return ret;
}

vector<long long> toDigits(long long N) {
    stringstream s;
    s << N;
    string digits = s.str();

    vector<char> temp(digits.begin(), digits.end());
    vector<long long> ret;

    for (auto it = temp.begin(); it != temp.end(); it++) {
        ret.push_back(*it - '0');
    }

    return ret;
}

long long makeTidy(long long N, vector<long long> digits, long long idx) {
    long long lsd = digits[digits.size() - 1];
    if (lsd != 9) {
        N = N - (lsd + 1);
        digits = toDigits(N);
    }

    // while?
    if (digits[idx] > digits[idx + 1]) {
        long long sub = exponent(10, digits.size() - (idx + 2));
        sub *= digits[idx + 1] + 1;
        N = N - sub;
        digits = toDigits(N);
    }

    return N;
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        long long N;
        cin >> N;

        vector<long long> digits = toDigits(N);
        for (long long j = digits.size() - 2; j >= 0; j--) {
            if (digits[j] > digits[j+1])  {
                // not tidy
                N = makeTidy(N, digits, j);
                digits = toDigits(N);
            }
        }

        cout << "Case #" << i+1 << ": " << N << endl;
    }
}
