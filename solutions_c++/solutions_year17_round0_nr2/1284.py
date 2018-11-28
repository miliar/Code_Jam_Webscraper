#include <iostream>

using namespace std;
typedef long long ll;

int main() {
      freopen("/Users/vino/Desktop/B-large.in", "r", stdin);
      freopen("/Users/vino/Desktop/B-large.out", "w", stdout);
    int T;
    cin >> T;
    char num[20];
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        cin >> num;
        ll ans = 0;
        int len = strlen(num);
        while (true) {
            ll ret = 0;
            bool flag = false;
            for (int i = 0; i < len; ++i) {
                if (i == len - 1 || (i + 1 < len && num[i] <= num[i + 1])) {
                    ret = ret * 10 + (num[i] - '0');
                } else {
                    ret = ret * 10 + (num[i] - '0' - 1);
                    for (int j = i + 1; j < len; ++j) {
                        ret = ret * 10 + 9;
                    }
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                ans = ret;
                break;
            }
            int c = 0;
            char s[20];
            while (ret) {
                s[c++] = ret % 10;
                ret /= 10;
            }
            for (int i = 0; i < c; i++) {
                num[i] = s[c - i - 1] + '0';
            }
            num[c] = '\0';
            len = c;
        }
        cout << ans << endl;

    }

    return 0;
}