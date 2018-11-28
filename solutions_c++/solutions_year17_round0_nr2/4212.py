#include <iostream>
#include <cstdio>
#include <string>

using i64 = long long;

using namespace std;

int main() {
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    int n;
    cin >> n;

    for (int test = 1; test <= n; test++) {
        cout << "Case #" << test << ": ";

        string s;
        cin >> s;
        s = "0" + s;

        string result;
        for (int i = (int)s.size() - 1; i > 0; i--) {
            if (s[i - 1] > s[i]) {
                s[i - 1]--;
                result.assign(result.size() + 1, '9');
            } else {
                result = s[i] + result;
            }
        }

        i64 ans = stoll(result);
        cout << ans << endl;
    }
}