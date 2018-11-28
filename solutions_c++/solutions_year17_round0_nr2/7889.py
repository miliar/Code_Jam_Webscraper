#include <iostream>
#include <vector>
using namespace std;

string getLastTidy() {
    string t;
    cin >> t;
    string s = "";
    for (int i = (int)t.size() - 1; i >= 0; i--) {
        s += t[i];
    }

    vector<char> v;
    v.push_back(s[0]);
    for (int i = 1; i < s.size(); i++) {
        if (s[i] > v[i - 1]) {
            for (int j = 0; j < i; j++) {
                v[j] = '9';
            }
            v.push_back(s[i] - 1);
        } else if (s[i] > 0) {
            v.push_back(s[i]);
        }
    }
    if (v.back() == '0') v.pop_back();
    string tidy = "";
    for (int i = (int)v.size() - 1; i >= 0; i--) {
        tidy += v[i];
    }
    return tidy;
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Case #" << i + 1 << ": " << getLastTidy() << endl;
    }
}
