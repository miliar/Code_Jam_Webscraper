#include <iostream>

using namespace std;

bool flip(string& s, int k, int pos) {
    int len = s.length();
    if (len-pos < k) return false;
    for (int i = pos; i < pos+k; ++i)
        s[i] = (s[i] == '+') ? '-' : '+';
    return true;
}

int findNextBlankSide(string s, int curPos) {
    int index = curPos;
    for (; index < s.length(); ++index)
        if (s[index] == '-')
            return index;
    return index;
}

int minFlips(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.length();) {
        i = findNextBlankSide(s, i);
        if (i == s.length()) return count;
        if (flip(s, k, i))
            count++;
        else
            return -1;
    }
}


int main() {
    int t, k;
    string s;
    cin >> t;
    for (int i = 1; i < t+1; ++i) {
        cin >> s >> k;
        cout << "Case #" << i << ": ";
            int res = minFlips(s, k);
            if (res >= 0)
                cout << res;
            else
                cout << "IMPOSSIBLE";
            cout << endl;
    }
    return 0;
}
