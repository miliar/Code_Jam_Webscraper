#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

string s;
vector<char> str;
int K;

bool flip(int indx) {
    if (indx + K > str.size()) return false;
    for (int i = indx; i < indx + K; i++) {
        if (str[i] == '-') str[i] = '+';
        else str[i] = '-';
    }
    return true;
}

int main() {

    ifstream cin ("input.txt");
    ofstream cout ("ans.txt");

    int T; cin >> T;
    for (int t = 1; t <= T; t++) {

        cin >> s;
        cin >> K;

        str.clear();
        for (int i = 0; i < s.size(); i++) {
            str.pb(s[i]);
        }

        bool can = true;
        int ans = 0;
        for (int i = 0; i < str.size(); i++) {
            if (str[i] == '-') {
                if (!flip(i)) {
                    can = false;
                    break;
                }
                ans++;
            }
        }

        cout << "Case #" << t << ": ";

        if (!can) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }

    return 0;
}