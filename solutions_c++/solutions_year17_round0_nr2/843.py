#include <bits/stdc++.h>

using namespace std;

vector <long long> v;

string toString(long long val) {
    stringstream ss;
    ss << val;
    return ss.str();
}

bool ok(string val) {
    char curDigit = '0';
    for (int i = 0; i < val.length(); i++) {
        if (val[i] < curDigit) return false;
        curDigit = val[i];
    }
    return true;
}

int main() {
    ifstream cin ("B-large.in");
    ofstream cout ("tidy.out");
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test;
    cin >> test;
    for (int ttest = 1; ttest <= test; ttest++) {
        cout << "Case #" << ttest << ": ";

        string s;
        cin >> s;
        if (ok(s)) {
            cout << s << "\n";
            continue;
        }

        v.clear();
        long long cur = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != '0') {
                long long tmp = cur * 10 + s[i] - '1';
                for (int j = i + 1; j < s.length(); j++) tmp = tmp * 10 + 9;
                if (ok(toString(tmp))) v.push_back(tmp);
            }
            cur = cur * 10 + s[i] - '0';
        }
        sort(v.begin(), v.end());

        cout << v.back() << "\n";
    }
}
