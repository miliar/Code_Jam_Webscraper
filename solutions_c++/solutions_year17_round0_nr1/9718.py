#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

template <typename T>
T read(istream& is);

int flipper(string s, int const k);

int main() {
    auto cases = read<int>(cin);

    for (auto i = 0; i < cases; ++i) {
        auto const s = read<string>(cin);
        auto const k = read<int>(cin);

        auto const flips = flipper(s, k);

        cout << "Case #" << i + 1 << ": ";

        if (flips < 0) cout << "IMPOSSIBLE" << '\n';
        else cout << flips << '\n';
    }
}

template <typename T>
T read(istream& is) {
    T t; is >> t;
    return t;
}

int flipper(string s, int const k) {
    auto result = 0;

    auto flip = [](auto& c) { c = (c == '+' ? '-' : '+'); };

    for (auto i = 0u; i < s.size() - (k - 1); ++i) {
        // Flip K pancakes if pancake is flat.
        if (s[i] == '-') {
            ++result;

            for (auto j = 0; j < k; ++j) flip(s[i + j]);
        }
    }

    if (s.find('-') != string::npos) return -1;

    return result;
}
