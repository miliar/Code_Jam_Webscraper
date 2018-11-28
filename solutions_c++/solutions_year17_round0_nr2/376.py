#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100 + 10;
const int INF = (int)(1e9);

vector<int> get_digits(long long n) {
    vector<int> d;
    while (n > 0) {
        d.push_back(n % 10);
        n /= 10;
    }
    reverse(d.begin(), d.end());
    return d;
}

long long gen_number(int num_digits, int num) {
    long long res = 0;
    for(int i = 1; i <= num_digits; ++i) res = res * 10 + num;
    return res;
}

bool build_res(int i, vector<int> &d, long long n, int min_digit, long long &num) {
    if (i > d.size()) return true;
    for(int x = 9; x >= min_digit; --x) {
        long long y = num;
        for(int j = i; j <= d.size(); ++j) y = y * 10 + x;
        if (y <= n) {
            num = num * 10 + x;
            return build_res(i + 1, d, n, x, num);
        }
    }
    return false;
}

void run() {
    long long n;
    cin >> n;
    vector<int> d = get_digits(n);
    long long res = 0;
    bool ok = build_res(1, d, n, 1, res);
    if (!ok) res = gen_number(d.size() - 1, 9);

    cout << res << endl;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int ntests = 1;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cout << "Case #" << tc << ": ";
        run();
    }
}
