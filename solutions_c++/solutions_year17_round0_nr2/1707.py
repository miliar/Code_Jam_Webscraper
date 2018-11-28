#include <iostream>
#include <vector>
#include <string>
using namespace std;

string solve(string s)
{
    int st = 0;
    while (st+1 < s.size() && s[st] <= s[st+1]) {
        st++;
    }
    //cerr << st << endl;
    if (st+1 == s.size()) {
        return s;
    }
    while (st > 0 && s[st-1] == s[st]) {
        st--;
    }
    //cerr << st << endl;
    s[st]--;
    for (int i = st + 1; i < s.size(); ++i) {
        s[i] = '9';
    }
    int start = 0;
    while (start + 1 < s.size() && s[start] == '0') {
        start++;
    }
    return s.substr(start);
}

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        string s;
        cin >> s;
        cout << "Case #" << cas << ": " << solve(s) << endl;
    }
}
