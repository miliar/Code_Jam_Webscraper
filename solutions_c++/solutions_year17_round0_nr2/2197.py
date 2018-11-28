#include <bits/stdc++.h>

using namespace std;

string s;
string cur;
string answer;

bool rec(int i, bool still_eq, char min_dig)
{
    if (i >= s.size()) {
        answer = cur;
        return true;
    }
    char upper = '9';
    if (still_eq) {
        upper = s[i];
    }
    for (char dig = upper; dig >= min_dig; dig--) {
        cur[i] = dig;
        if (rec(i + 1, still_eq and dig == s[i], dig)) {
            return true;
        }
    }
    return false;
}

void solve(int test_num)
{
    cin >> s;

    cur.resize(s.size());
    answer = "";
    if (not rec(0, true, '1')) {
        for (int i = 0; i < s.size() - 1; i++) {
            answer.push_back('9');
        }
    }
    cout << "Case #" << test_num << ": " << answer << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        solve(i);
    }
}
