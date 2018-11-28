#include <bits/stdc++.h>
#include <ext/numeric>
using namespace std;  // NOLINT
using namespace __gnu_cxx;
using LL = int64_t;
const int INF = 0x3f3f3f3f;
const LL mod = 1000000007;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin >> t;
    int k = t;
    while (t--) {
        cout << "Case #" << k - t << ": ";
        string s;
        cin >> s;
        if (s.length() == 1) cout << s << endl;
        else {
            string t = "";
            for (int i = 0; i < s.length() - 1; i++) {
                t += s[i];
                if (s[i] > s[i + 1]) {
                    t[i]--;
                    int k = i;
                    for (k--; k >= 0; k--) {
                        if (t[k + 1] < t[k]) {
                            t[k]--;
                        } else break;
                    }
                    k++;
                    t = t.substr(0, k + 1);
                    for (int j = k + 1; j < s.length(); j++) t += "9";
                    break;
                } else {
                    if (i + 1 == s.length() - 1) t += s[i + 1];
                }
            }
            stringstream ss;
            ss << t;
            LL k;
            ss >> k;
            cout << k << endl;
        }
    }
}
