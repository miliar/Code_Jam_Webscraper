#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define pb push_back
#define mp make_pair

int n, p;
int a[111];

void solve(){
    cin >> n >> p;
    for(int i = 0; i < n; i++) cin >> a[i];
    int md[4] = {};
    for(int i = 0; i < n; i++){
        md[ a[i] % p ]++;
    }
    int ans = md[0];
    if(p == 2){
        ans += (md[1] + 1) / 2;
    }
    if(p == 3){
        ans += min(md[1], md[2]);
        int mn = min(md[1], md[2]);
        md[1] -= mn;
        md[2] -= mn;
        ans += md[1] / 3;
        md[1] %= 3;
        ans += md[2] / 3;
        md[2] %= 3;
        if(md[1] || md[2]) ans++;
    }
    if(p == 4){

    }
    cout << ans << endl;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    int test;
    cin >> test;
    for(int i = 1; i <= test; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
