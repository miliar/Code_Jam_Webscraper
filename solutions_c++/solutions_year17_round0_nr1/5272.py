#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int (i)=(0);(i)<(int)(n);++(i))
typedef pair<int, int> P;
typedef long long ll;

const string no = "IMPOSSIBLE";

inline void output(int i, int n) {
    cout << "Case #" << i+1 << ": " << n << endl;
}

inline void imp(int i) {
    cout << "Case #" << i+1 << ": " << no << endl;
}

int main() {
    ios::sync_with_stdio();
    cin.tie(0);

    int n;
    cin >> n;

    rep(i, n) {
        int k, ans=0;
        string s;
        cin >> s >> k;

        rep(i, s.size()) {
            if (s[i] == '-' && i+k-1 < s.size()) {
                for (int j=i; j<min((int)s.size(), i+k); ++j) {
                    s[j]=(s[j] == '+' ? '-' : '+');
                }
                ans++;
            }
        }

        bool flag=true;
        rep(i, s.size()) {
            if (s[i] == '-') {
                flag=false;
                break;
            }
        }

        if (flag) {
            output(i, ans);
        }
        else {
            imp(i);
        }
    }
}
