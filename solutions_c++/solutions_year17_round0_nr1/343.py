
#include <iostream>
#include <string>

using namespace std;

string solve() {
    string s;
    int k;
    cin >> s >> k;

    int cnt = 0;
    for (int i = 0; i + k <= s.size(); i++) {
        if (s[i] == '-') {
            for (int j = i; j < i + k; j++)
                s[j] = (s[j] == '-' ? '+' : '-');
            cnt++;
        }
    }
    for (int i = 0; i < s.size(); i++)
        if (s[i] == '-')
            return "IMPOSSIBLE";
    return to_string(cnt);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }
}
