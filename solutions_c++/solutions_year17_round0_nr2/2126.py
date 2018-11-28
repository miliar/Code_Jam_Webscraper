#include <iostream>

using namespace std;

long long ans[1000];

int b[1000];

int main() {
    //freopen("/Users/philip/Downloads/B-large.in", "r", stdin);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        int m = (int)s.size();
        ans[m - 1] = s[m - 1] - '0';
        b[m - 1] = s[m - 1] - '0';
        long long d = 10;
        for (int j = m - 2; j >= 0; j--, d *= 10) {
            if (s[j] - '0' <= b[j + 1]) {
                ans[j] = ans[j + 1];
                ans[j] += (s[j] - '0') * d;
                b[j] = s[j] - '0';
            }
            else {
                b[j] = s[j] - '1';
                ans[j] = (s[j] - '0') * d - 1;
            }
        }
        cout << "Case #" << i + 1 << ": " << ans[0] << '\n';
    }
}
