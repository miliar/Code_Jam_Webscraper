#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        string s;
        int k;
        cin >> s >> k;
        int cnt = 0;
        for (int i = 0; i + k <= (int)s.length(); ++i)
            if (s[i] == '-') {
                for (int j = 0; j < k; ++j)
                    s[i + j] = s[i + j] == '+' ? '-' : '+';
                ++cnt;
            }
        bool happy = true;
        for (int i = s.length() - k + 1; i < (int)s.length() && happy; ++i)
            happy = s[i] == '+';
        if (happy)
            cout << cnt << endl;
        else
            cout << "IMPOSSIBLE\n";
    }
    return 0;
}