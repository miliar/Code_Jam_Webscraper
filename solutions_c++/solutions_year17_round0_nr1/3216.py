#include <iostream>
#include <fstream>

using namespace std;

string flip(string s, int i, int k) {
    for (int j = 0; j < k; j++) 
        s[i + j] = (s[i + j] == '+') ? '-' : '+';
    return s;
}

string reverse(string s) {
    string ret = s;
    for (int i = 0; i < s.size(); i++) {
        ret[i] = s[s.size() - 1 - i];
    }
    return ret;
}

bool check(string s) {
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '-') return false;
    }
    return true;
}

int main() {
    ifstream cin ("in.txt");
    ofstream cout ("out.txt");
    int T;
    string s;
    int k;
    cin >> T;
    for (int cs = 1; cs <= T; cs++) {
        cin >> s >> k;
        string old = s;
        int ans = s.size();
        int count = 0;
        for (int i = 0; i < s.size() + 1 - k; i++) {
            if (s[i] == '-') {
                s = flip(s, i, k);
                count++;
                // cout << count << ' ' << s << endl;
            }
        }
        if (check(s))
            ans = min(count, ans);
        s = reverse(old);
        count = 0;
        for (int i = 0; i < s.size() + 1 - k; i++) {
            if (s[i] == '-') {
                s = flip(s, i, k);
                count++;
                // cout << count << ' ' << s << endl;
            }
        }
        if (check(s))
            ans = min(count, ans);
        cout << "Case #" << cs << ": ";
        if (ans == s.size()) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }   
}