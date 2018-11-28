#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <iomanip>
using namespace std;
typedef long long ll;
typedef long double ld;

template<typename T>
class IntegerIterator {
public:
    using value_type = T;

    constexpr explicit IntegerIterator(const value_type value) : value_(value) {}

    IntegerIterator& operator++() {
        ++value_;
        return *this;
    }

    constexpr value_type operator*() const {
        return value_;
    }

    constexpr bool operator ==(const IntegerIterator rhs) const {
        return value_ == rhs.value_;
    }

    constexpr bool operator !=(const IntegerIterator rhs) const {
        return !(*this == rhs);
    }

private:
    value_type value_;

};

template<typename T>
class IntegerRange {
public:
    using const_iterator = IntegerIterator<T>;

    constexpr IntegerRange(const T begin, const T end) : begin_(begin), end_(end) {}

    constexpr const_iterator begin() const {
        return const_iterator(begin_);
    }

    constexpr const_iterator end() const {
        return const_iterator(end_);
    }

private:
    T begin_;
    T end_;
};
template<typename T>
constexpr IntegerRange<T> range(const T from, const T to) {
    return IntegerRange<T>(from, to);
}

void print(int test, const string& ans) {
    cout << "Case #" << test << ": " << ans << "\n";
}

const int maxN = 111;
int d[maxN][maxN][maxN][4];

int main(void) {
    ios_base::sync_with_stdio(0);cout.setf(ios::fixed);cout.precision(10);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        int n, p;
        cin >> n >> p;
        int ans = 0;
        int cnt[4] = {0, 0, 0, 0};
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            if (x % p == 0) {
                ans++;
            } else {
                cnt[x % p]++;
            }
        }
        d[0][0][0][0] = 0;
        d[0][0][0][1] = -1e9;
        d[0][0][0][2] = -1e9;
        d[0][0][0][3] = -1e9;
        for (int i : range(0, cnt[1] + 1)) {
            for (int j : range(0, cnt[2] + 1)) {
                    for (int k : range(0, cnt[3] + 1)) {
                    if (i + j + k == 0) continue;
                    d[i][j][k][0] = -1e9;
                    d[i][j][k][1] = -1e9;
                    d[i][j][k][2] = -1e9;
                    d[i][j][k][3] = -1e9;
                    for (int rem = 0; rem < p; rem++) {
                        if (i) {
                            int pp = (rem - 1 + p) % p;
                            d[i][j][k][rem] = max(d[i][j][k][rem],
                                                  d[i - 1][j][k][pp] + (pp == 0));
                        }
                        if (j) {
                            int pp = (rem - 2 + p) % p;
                            d[i][j][k][rem] = max(d[i][j][k][rem],
                                                  d[i][j - 1][k][pp] + (pp == 0));
                        }
                        if (k) {
                            int pp = (rem - 3 + p) % p;
                            d[i][j][k][rem] = max(d[i][j][k][rem],
                                                  d[i][j][k - 1][pp] + (pp == 0));
                        }
                    }
                }
            }
        }
        int mx = ans + max(max(d[cnt[1]][cnt[2]][cnt[3]][0], d[cnt[1]][cnt[2]][cnt[3]][1]),
                           max(d[cnt[1]][cnt[2]][cnt[3]][2], d[cnt[1]][cnt[2]][cnt[3]][3]));
        print(test, to_string(mx));
    }
    return 0;
}
