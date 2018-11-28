#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

#define PROBLEM "B-large"

using namespace std;

bool tidyfy(vector<int>& v, int n, int m) {
    if (v[n - 1] < m) {
        return false;
    } else if (n == 1) {
        return true;
    } else if (tidyfy(v, n-1, v[n-1])) {
        return true;
    } else if (v[n-1] - 1 < m) {
        return false;
    } else {
        --v[n-1];
        for (int i = 0; i < n-1; ++i) v[i] = 9;
        return true;
    }
}

long long solve(long long n) {
    vector<int> v;
    v.reserve(30);
    while (n) {
        v.push_back(n % 10);
        n /= 10;
    }
    tidyfy(v, v.size(), 0);
    long long res = 0;
    for (int i = v.size() - 1; i >= 0; --i) {
        res = res * 10 + v[i];
    }
    return res;
}

int main()
{
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        long long n;
        cin >> n;
        cout << "Case #" << t << ": " << solve(n) << endl;
    }
    return 0;
}
