#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define pb push_back
#define mp make_pair

int k;
string s;

void solve()
{
    cin >> s >> k;
    int n = s.length();
    int cnt = 0;
    for(int i = 0; i < n - k + 1; i++){
        if(s[i] == '-'){
            cnt++;
            for(int j = i; j < i + k; j++){
                if(s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
        }
    }
    bool ok = true;
    for(int i = 0; i < n; i++) if(s[i] == '-') ok = false;
    if(ok) cout << cnt << endl;
    else cout << "IMPOSSIBLE" << endl;
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("output.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    int tests;
    cin >> tests;
    for(int i = 1; i <= tests; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}





