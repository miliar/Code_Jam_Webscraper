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
const int maxN = 1e3 + 10;
int cnt[maxN][maxN];
int main(void) {
    ios_base::sync_with_stdio(0);cout.setf(ios::fixed);cout.precision(10);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        int n, m, c;
        cin >> n >> c >> m;
        for (int i : range(1, n + 1)) {
            for (int j : range(1, c + 1)) {
                cnt[i][j] = 0;
            }
        }
        for (int i : range(1, m + 1)) {
            int p, b;
            cin >> p >> b;
            cnt[p][b]++;
        }
        int mx = 0;
        for (int j : range(1, c + 1)) {
            int sum = 0;
            for (int i : range(1, n + 1)) {
                sum += cnt[i][j];
            }
            mx = max(sum, mx);
        }
        int extraPlaces = 0;
        int ans = mx;
        int promotions = 0;
        for (int i : range(1, n + 1)) {
            int sum = 0;
            for (int j : range(1, c + 1)) {
                sum += cnt[i][j];
            }
            if (sum <= ans) {
                extraPlaces += ans - sum;
                continue;
            }
            if (extraPlaces >= sum - ans) {
                extraPlaces -= (sum - ans);
                promotions += (sum - ans);
            } else {
                ans++;
                extraPlaces += (i - 1);
                i--;
            }
        }
        print(test, to_string(ans) + " " + to_string(promotions));
    }
    return 0;
}
