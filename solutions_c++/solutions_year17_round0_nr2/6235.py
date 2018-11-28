#include <bits/stdc++.h>
using namespace std;
#define DB(v) cerr << #v << ' ' << v << endl
#define sz(v) int(v.size())
#define For(i, a, b) for(int i = a;i <= b; ++i)

bool good (string &s, int pos, int val) {
    for(int i = pos;i < sz(s); ++i) {
        if(s[i] > val)
            return true;
        if(s[i] < val)
            return false;
    }
    return true;
}

int main()
{
#ifdef HOME
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // HOME
    int T; cin >> T;

    string s;
    For(t, 1, T) {
        cin >> s;
        string res = "";
        for(int i = 0;i < sz(s); ++i) {
            if(good(s, i, s[i])) {
                res += s[i];
            }
            else {
                char c = s[i]; c--;
                res += c;
                for(int j = i + 1;j < sz(s); ++j) {
                    res += '9';
                }
                break;
            }
        }
        if(res[0] == '0')
            res = res.substr(1);
        cout << "Case #" << t << ": " << res << '\n';
    }
    return 0;
}
