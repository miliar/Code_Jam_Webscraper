#include <iostream>
#include <fstream>

using namespace std;

ifstream in("A-large.in");
ofstream out("A-large.out");

//#define out cout

char flip(string &s, int pos, int k) {
    for (int i = pos; i < pos + k; ++i)
        if (s[i] == '-') s[i] = '+';
        else s[i] = '-';
}

int main() {
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        string s;
        int k;
        in >> s >> k;
        int ans = 0;
        for (int j = 0; j <= s.size() - k; ++j) {
            if (s[j] == '-') {
                flip(s, j, k);
                ++ans;
            }
        }
        for (int j = s.size() - k + 1; j < s.size(); ++j)
            if (s[j] == '-') {
                ans = -1;
                break;
            }
        out << "Case #" << i + 1 << ": ";
        if (ans == -1) out << "IMPOSSIBLE\n";
        else out << ans << '\n';
    }
    return 0;
}
