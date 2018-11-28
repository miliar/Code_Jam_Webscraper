#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define pb push_back
#define mp make_pair

string s;

void solve()
{
    cin >> s;
    int n = s.length();
    while(1){
        bool ok = false;
        for(int i = 1; i < n; i++){
            if(s[i] >= s[i - 1]) continue;
            s[i - 1]--;
            for(int j = i; j < n; j++) s[j] = '9';
            ok = true;
            break;
        }
        if(!ok) break;
    }
    if(s[0] == '0') cout << s.substr(1, n - 1) << endl;
    else cout << s << endl;
}

int main()
{
    freopen("B.in", "r", stdin);
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





