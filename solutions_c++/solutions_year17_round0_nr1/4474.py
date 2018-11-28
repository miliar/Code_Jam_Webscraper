#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int maxn = 1e3 + 1, inf = 1e9 + 100, mod = 1e9 + 7;

int test;

char mk(char c){
    if (c == '+')
        return '-';
    return '+';
}

int main(){
    #ifdef ONPC
    ifstream cin("a.in");
    ofstream cout("a.out");
    #else
    //ifstream cin("a.in");
    //ofstream cout("a.out");
    #endif // ONPC
    ios::sync_with_stdio(0);
    cin >> test;
    for (int iter = 1; iter <= test; iter++){
        bool a[maxn];
        memset(a, 0, sizeof(a));
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        int cnt = 0;
        int ans = 0;
        for (int i = 0; i < n; i++){
            if (a[i])
                cnt--;
            if (cnt % 2 == 1)
                s[i] = mk(s[i]);
            if (s[i] == '-'){
                if (i + k > n){
                    ans = -1;
                    break;
                }
                a[i + k] = 1;
                cnt++;
                ans++;
            }
        }
        cout << "Case #" << iter << ": ";
        if (ans == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << '\n';
    }
}
