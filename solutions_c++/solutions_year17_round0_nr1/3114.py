#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair


int main()
{
    ios::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int r=0; r<T; r++) {
        bool flag = true;
        int k, ans = 0;
        string s;
        cin >> s >> k;
        for (int i=0; i<(int)s.length(); i++) {
            if (s.at(i) == '-') {
                if ((int)s.length() - i < k) {
                    flag = false;
                    break;
                } else {
                    ans ++;
                    for (int j=i; j<k+i; j++) {
                        if (s.at(j) == '-') s.at(j) = '+';
                        else s.at(j) = '-';
                    }
                }
            }
        }
        if (flag) cout << "Case #" << r+1 << ": " << ans << '\n';
        else cout << "Case #" << r+1 << ": IMPOSSIBLE" << '\n';
    }
    return 0;
}
