#include <iostream>
#include <string>

using namespace std;

string numOfFlip(string &s, int K) {
    auto i = s.find('-');
    int count = 0;
    while (i < s.size()) {
        if (s[i] == '-' && i + K <= s.size()) {
            for (auto j = i; j != i + K; ++j) s[j] = s[j] == '+' ? '-' : '+';
            count++;
            // cout << i << endl;
        }
        // cout << s << endl;
        i++;
    }
    for (auto j = 0; j != s.size(); ++j) if (s[j] == '-') return "IMPOSSIBLE";
    return to_string(count);
}

int main() {
    int T, id = 1;
    string s;
    int K;
    cin >> T;
    while (T--) {
        cout << "Case #" << id << ": ";
        cin >> s >> K;
        id++;
        cout << numOfFlip(s, K) << endl;
    }

    return 0;
}