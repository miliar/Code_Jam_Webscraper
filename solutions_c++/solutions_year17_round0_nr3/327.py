#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

#include <cassert>
using namespace std;

struct TData {
    long long Size;
    long long LeftDistance;
    long long RightDistance;

    long long GetMinDistance() const noexcept {
        return min(LeftDistance, RightDistance);
    }

    long long GetMaxDistance() const noexcept {
        return max(LeftDistance, RightDistance);
    }
};

bool operator < (const TData& lhs, const TData& rhs) noexcept {
    return lhs.GetMinDistance() > rhs.GetMinDistance() ||
        (lhs.GetMinDistance() == rhs.GetMinDistance() && lhs.GetMaxDistance() > rhs.GetMaxDistance());
}

long long n, k;
map<TData, long long> mp;

TData GetDataBySize(const long long s) noexcept {
    const long long leftDistance = ((s & 1) ? (s >> 1) + 1 : (s >> 1));
    const long long rightDistance = (s >> 1) + 1;
    return TData{s, leftDistance, rightDistance};
}

pair<long long, long long> Divide(const long long s) noexcept {
    return make_pair((s - 1) >> 1, s >> 1);
}

pair<long long, long long> GetFastResult(long long n, long long k) {
    mp.clear();
    mp[GetDataBySize(n)] += 1;
    while (k > 0) {
        long long count = mp.begin()->second;
        if (k <= count) {
            return make_pair(
                mp.begin()->first.GetMaxDistance(),
                mp.begin()->first.GetMinDistance());
        } else {
            k -= count;
            const long long s = mp.begin()->first.Size;
            mp.erase(mp.begin());
            const auto ps = Divide(s);
            if (ps.first > 0) {
                mp[GetDataBySize(ps.first)] += count;
            }
            if (ps.second > 0) {
                mp[GetDataBySize(ps.second)] += count;
            }
        }
    }
    assert(false);
}

pair<long long, long long> GetSlowResult(int n, int k) {
    static vector<bool> used;
    static vector<int> leftDistance;
    static vector<int> rightDistance;
    used.assign(n, false);
    leftDistance.resize(n);
    rightDistance.resize(n);
    for (int i = 0; i < k; ++i) {
        int leftPos = -1;
        for (int j = 0; j < n; ++j) {
            if (used[j]) {
                leftPos = j;
            } else {
                leftDistance[j] = j - leftPos;
            }
        }
        int rightPos = n;
        for (int j = n - 1; j >= 0; --j) {
            if (used[j]) {
                rightPos = j;
            } else {
                rightDistance[j] = rightPos - j;
            }
        }

        int resultPos = -1;
        int rmn;
        int rmx;
        for (int j = 0; j < n; ++j) {
            if (used[j]) {
                continue;
            }
            if (resultPos == -1) {
                resultPos = j;
            } else {
                int cmn = min(leftDistance[j], rightDistance[j]);
                int cmx = max(leftDistance[j], rightDistance[j]);
                if (rmn < cmn || (rmn == cmn && rmx < cmx)) {
                    resultPos = j;
                }
            }
            rmn = min(leftDistance[resultPos], rightDistance[resultPos]);
            rmx = max(leftDistance[resultPos], rightDistance[resultPos]);
        }

        used[resultPos] = true;

        if (i == k - 1) {
            return pair<long long, long long>(rmx, rmn);
        }
    }
    assert(false);
}

void DoTest() {
    for (long long n = 1; n <= 1000; ++n) {
        for (long long k = 1; k <= n; ++k) {
            const auto result = GetFastResult(n, k);
            const auto slowResult = GetSlowResult(n, k);
            if (slowResult != result) {
                cout << "Fail on n = " << n << " and k = " << k << endl;
                return;
            } else {
                cout << "Ok on n = " << n << " and k = " << k << endl;
            }
        }
    }
}

void Solve() {
    const auto result = GetFastResult(n, k);
    cout << result.first - 1 << " " << result.second - 1 << endl;
}

void Read() {
    cin >> n >> k;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        Read();
        cout << "Case #" << test << ": ";
        Solve();
    }

    return 0;
}
