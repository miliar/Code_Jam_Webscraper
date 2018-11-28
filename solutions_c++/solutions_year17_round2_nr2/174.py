#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

const string impossible = "IMPOSSIBLE\n";

void solve(int)
{
    int n;
    cin >> n;
    vector<pair<int, int>> v(3); // base color, complement
    vector<pair<char, char>> name = {{'R', 'G'}, {'Y', 'V'}, {'B', 'O'}};
    cin >> v[0].first >> v[2].second >> v[1].first >> v[0].second >> v[2].first >> v[1].second;

    vector<int> count_left(3);
    for (int i = 0; i < 3; ++i) count_left[i] = v[i].first - v[i].second;

    int x = 0;
    for (int i = 0; i < 3; ++i) {
        int j = count_left[i];
        if (j < 0) {
            cout << impossible;
            return;
        }
        if (j == 0 && v[i].second > 0) ++x;
    }
    if (x > 1 || (x == 1 && count_left[0] + count_left[1] + count_left[2] > 0)) {
        cout << impossible;
        return;
    }

    auto swap_colors = [&](int a, int b) {
        swap(count_left[a], count_left[b]);
        swap(v[a], v[b]);
        swap(name[a], name[b]);
    };

    auto sort_colors = [&]() {
        if (count_left[0] < count_left[1]) swap_colors(0, 1);
        if (count_left[1] < count_left[2]) swap_colors(1, 2);
        if (count_left[0] < count_left[1]) swap_colors(0, 1);
    };

    sort_colors();

    if (count_left[0] > count_left[1] + count_left[2]) {
        cout << impossible;
        return;
    }

    string result;
    if (count_left[0] + count_left[1] + count_left[2] > 0) {
        result += name[0].first;
        --count_left[0];
        while (count_left[0] + count_left[1] + count_left[2] > 0) {
            sort_colors();
            int next = 0;
            if (name[next].first == result.back()) next = 1;
            result += name[next].first;
            --count_left[next];
        }
    }

    int size = result.size();

    if (size == 0) {
        assert((v[0].second > 0) + (v[1].second > 0) + (v[2].second > 0) <= 1);
        for (int i: {0, 1, 2}) {
            for (int j = 0; j < v[i].second; ++j) {
                result += name[i].first;
                result += name[i].second;
            }
        }

    } else {
        if (result.back() == result.front()) {
            assert(result.size() > 2);
            assert(result[size - 3] != result[size - 1]);
            swap(result[size - 2], result[size - 1]);
        }

        for (int i: {0, 1, 2}) {
            string t;
            for (int j = 0; j < v[i].second; ++j) {
                t += name[i].first;
                t += name[i].second;
            }
            if (t.size()) {
                size_t pos = 0;
                while (pos < result.size() && result[pos] != name[i].first) ++pos;
                assert(result[pos] == name[i].first);
                result = result.substr(0, pos) + t + result.substr(pos);
            }
        }
    }

    assert(result.back() != result.front());
    for (int i = 1; i < result.size(); ++i) {
        assert(result[i - 1] != result[i]);
    }

    cout << result << endl;
}

int32_t main()
{
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve(i);
    }
}
