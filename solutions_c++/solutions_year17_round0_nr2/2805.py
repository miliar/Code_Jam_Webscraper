#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;



int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int ttt = 1; ttt <= T; ++ttt) {
        string s;
        cin >> s;
        for (size_t i = 0; i + 1 < s.size(); ++i) {
            if (s[i] > s[i + 1]) {
                int cur = i;
                while (cur >= 0 && s[cur] == s[i])
                    --cur;
                int nxt = ++cur;
                while (s[cur]-- == '0')
                    s[cur--] = '9';
                cur = nxt + 1;
                while (cur < (int)s.size())
                    s[cur++] = '9';
                break;
            }
        }
        while (s.size() > 1 && s[0] == '0')
            s.erase(0, 1);
        cout << "Case #" << ttt << ": " << s << "\n";
    }

    return 0;
}
