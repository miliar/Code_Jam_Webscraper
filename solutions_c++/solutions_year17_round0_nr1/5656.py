#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

string pancake(string s, int k) {
    if (!s.size()) return "IMPOSSIBLE";
    if (s.find('-') == string::npos) return "0";
    if (k > s.size()) return "IMPOSSIBLE";

    int cnt = 0;

    for (int i = 0; i <= s.size() - k; ++i) {
        if ('-' == s[i]) {
            for (int j = i; j < i + k; ++j) {
                if ('-' == s[j]) s[j] = '+';
                else s[j] = '-';
            }
            ++cnt;
        }
    }

    for (int i = s.size() - k; i < s.size(); ++i) {
        if ('-' == s[i]) return "IMPOSSIBLE";
    }

    return to_string(cnt);
}

int main(int argc, char **argv) {
    int n;
    string s;
    int k;

    string res;

    cin>> n;

    //cout<< pancake("---+-++-", 3)<< endl;
    for (int i = 1; i <= n; ++i) {
        cin>> s>> k;
        res = pancake(s, k);
        cout<< "Case #"<< i<< ": "<< res<< endl;
    }

    return 0;
}
