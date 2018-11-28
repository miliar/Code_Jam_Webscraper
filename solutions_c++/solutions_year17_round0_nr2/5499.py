#include <bits/stdc++.h>

using namespace std;

typedef  unsigned long long int ull;

const ull MAXM = ull(1e18);

vector<ull> numbers;

void go(ull n) {
    if(n > MAXM) return;
    if(n > 0)
        numbers.push_back(n);
    int last_digit = n % 10;
    for(int i = max(last_digit, 1); i <= 9; ++i)
        go(n * 10 + i);
}

ull solve(ull n) {
    int low = 0, high = numbers.size() - 1;
    while(high - low > 1) {
        int mid = (low + high) / 2;
        if(numbers[mid] < n)
            low = mid;
        else
            high = mid;
    }

    return (numbers[high] <= n ? numbers[high] : numbers[low]);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    go(0);
    sort(numbers.begin(), numbers.end());

    int T;
    ull n;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cin >> n;
        cout << "Case #" << t << ": ";
        cout << solve(n) << '\n';
    }
}
