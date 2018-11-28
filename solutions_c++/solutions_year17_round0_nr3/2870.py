#include <iostream>

using namespace std;

void printResult(long long nr, pair<long long, long long> result) {
    cout << "Case #" << nr << ": " << result.first << " " << result.second << "\n";
}

pair<long long, long long> f(long long n, long long k) {
    if (n%2 == 0) {
        if (k == 1) {
            return make_pair(n/2, n/2 - 1);
        }

        if ((k-1)%2 == 1) {
            return f(n/2, (k-1)/2 + 1);
        }
        else {
            return f(n/2 - 1, (k-1)/ 2);
        }
    }
    else {
        if (k == 1) {
            return make_pair(n/2, n/2);
        }

        if ((k-1)%2) {
            return f(n/2, (k-1)/2 + 1);
        }
        else {
            return f(n/2, (k-1)/2);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);

    int t;
    long long n, k;
    pair<long long, long long> result;

    cin >> t;

    for (int i = 1; i <= t; i++) {
        cin >> n >> k;

        result = f(n, k);
        printResult(i, result);
    }

    return 0;
}