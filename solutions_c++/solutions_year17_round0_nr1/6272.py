#include <bits/stdc++.h>
using namespace std;
#define DB(v) cerr << #v << ' ' << v << endl
#define sz(v) int(v.size())
#define For(i, a, b) for(int i = a;i <= b; ++i)

bool good (string &s) {
    for(int i = 0;i < sz(s); ++i) {
        if(s[i] != '+')
            return false;
    }
    return true;
}

char change (char x) {
    if(x == '+')
        return '-';
    else if(x == '-')
        return '+';
}

int main()
{
#ifdef HOME
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // HOMe
    int T; cin >> T;

    string s;
    int k;
    For(t, 1, T) {
        cout << "Case #" << t << ": ";
        cin >> s; cin >> k;
        int n = sz(s);
        int res = 0;
        for(int i = 0;i + k - 1 < n; ++i) {
            if(s[i] == '-') {
                for(int j = i;j <= i + k - 1; ++j) {
                    s[j] = change(s[j]);
                }
                res++;
            }
        }
        if(!good(s))
            cout << "IMPOSSIBLE";
        else
            cout << res;
        cout << '\n';
    }
    return 0;
}
