#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair


string s;

void solve() {
    for (int i=0; i<(int)s.length()-1; i++) {
        if ((int)s.at(i) > (int)s.at(i+1)) {
            s.at(i) --;
            for (int j=i+1; j<(int)s.length(); j++) s.at(j) = (char)57;
            solve();
            return;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int r=0; r<T; r++) {
        cin >> s;
        solve();
        int i=0;
        while (s.at(i) == '0') i++;
        cout << "Case #" << r+1 << ": " << s.substr(i) << '\n';
    }
    return 0;
}
