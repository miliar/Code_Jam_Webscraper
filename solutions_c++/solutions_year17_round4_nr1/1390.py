#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        int n, p;
        cin >> n >> p;
        if (p == 2) {
            int mod0 = 0;
            int mod1 = 0;
            for (int i = 0; i < n; i++) {
                int k;
                cin >> k;
                if (k % 2 == 0) {
                    mod0++;
                } else {
                    mod1++;
                }
            }
            vector<int> v;
            while (mod0 > 0) {
                v.push_back(0);
                mod0--;
            }
            while (mod1 > 0) {
                v.push_back(1);
                mod1--;
            }
            int rc = 0;
            int ans = 0;
            for (int i = 0; i < n; i++) {
                if (rc == 0) {
                    ans++;
                }
                rc = (rc + v[i]) % 2;
            }
            cout << ans << endl;
        } else if (p == 3) {
            int mod0 = 0;
            int mod1 = 0;
            int mod2 = 0;
            for (int i = 0; i < n; i++) {
                int k;
                cin >> k;
                if (k % 3 == 0) {
                    mod0++;
                } else if (k % 3 == 1) {
                    mod1++;
                } else {
                    mod2++;
                }
            }
            vector<int> v;
            while (mod0 > 0) {
                v.push_back(0);
                mod0--;
            }
            while (mod1 > 0 && mod2 > 0) {
                v.push_back(2);
                v.push_back(1);
                mod1--;
                mod2--;
            }
            while (mod1 > 0) {
                v.push_back(1);
                mod1--;
            }
            while (mod2 > 0) {
                v.push_back(2);
                mod2--;
            }
            int rc = 0;
            int ans = 0;
            for (int i = 0; i < n; i++) {
                if (rc == 0) {
                    ans++;
                }
                rc = (rc + v[i]) % 3;
            }
            cout << ans << endl;
        } else {
            int mod0 = 0;
            int mod1 = 0;
            int mod2 = 0;
            int mod3 = 0;
            for (int i = 0; i < n; i++) {
                int k;
                cin >> k;
                if (k % 4 == 0) {
                    mod0++;
                } else if (k % 4 == 1) {
                    mod1++;
                } else if (k % 4 == 2) {
                    mod2++;
                } else {
                    mod3++;
                }
            }
            vector<int> v;
            while (mod0 > 0) {
                v.push_back(0);
                mod0--;
            }
            while (mod2 >= 2) {
                v.push_back(2);
                v.push_back(2);
                mod2 -= 2;
            }
            while (mod1 > 0 && mod3 > 0) {
                v.push_back(1);
                v.push_back(3);
                mod1--;
                mod3--;
            }
            while (mod2 > 0) {
                v.push_back(2);
                mod2--;
            }
            while (mod1 > 0) {
                v.push_back(1);
                mod1--;
            }
            while (mod3 > 0) {
                v.push_back(3);
                mod3--;
            }
            int rc = 0;
            int ans = 0;
            for (int i = 0; i < n; i++) {
                if (rc == 0) {
                    ans++;
                }
                rc = (rc + v[i]) % 4;
            }
            cout << ans << endl;
        }
    }  
    return 0;
}