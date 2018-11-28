#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

string s;
int k;

char GetFlipped(char c) {
    if (c == '-') {
        return '+';
    } else {
        return '-';
    }
}

void DoFlip(int pos) {
    for (int i = pos; i < pos + k; ++i) {
        s[i] = GetFlipped(s[i]);
    }
}

const string IMPOSSIBLE = "IMPOSSIBLE";

void Solve() {
    int result = 0;
    const int n = s.length();
    for (int i = 0; i + k <= n; ++i) {
        if (s[i] == '-') {
            DoFlip(i);
            ++result;
        }
    }
    for (int i = 0; i < n; ++i) {
        if (s[i] == '-') {
            cout << IMPOSSIBLE << endl;
            return;
        }
    }
    cout << result << endl;
}

void Read() {
    cin >> s >> k;
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
