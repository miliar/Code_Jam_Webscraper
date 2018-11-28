#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair <int, int> pii;

#define SZ(c) c.size()
#define ALL(c) c.begin(), c.end()
#define endl '\n'

const int N = 1e5 + 9;

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("outp.txt", "w", stdout);
#endif

    int cases;
    cin >> cases;
    for (int c = 1; c <= cases; ++c) {
        string s;
        cin >> s;

        if (s.size() == 1) {
            cout << "Case #" << c << ": " << s << endl;
            continue;
        }

        for (int i = 1; i < s.size(); ++i) {
            if (s[i] < s[i - 1]) {
                --s[i - 1];
                for (int j = i; j < s.size(); ++j) {
                    s[j] = '9';
                }

                for (int j = i - 1; j > 0; --j) {
                    if (s[j] >= s[j - 1])
                        break;
                    s[j] = '9';
                    --s[j - 1];
                }

                break;
            }
        }

        if (s[0] == '0')
            s = s.substr(1);

        cout << "Case #" << c << ": " << s << endl;
    }
    return 0;
}
