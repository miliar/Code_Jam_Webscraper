#include<bits/stdc++.h>

#define x first
#define y second
#define y0 hi1
#define y1 hi2
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(a) (a)*(a)
#define ld long double
#define all(a) (a).begin(), (a).end()

using namespace std;

const int inf = 2000000000;

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;
    for(int num = 1; num <= T; num++){
        cout << "Case #" << num << ": ";
        string s;
        cin >> s;
        int n = s.length();
        int k;
        cin >> k;

        int a[n + 1];
        memset(a, 0, sizeof(a));

        int ans = 0;
        bool ok = true;
        for(int v = 0, i = n - 1; i >= 0; i--){
            v += a[i];
            int cur = (s[i] == '-') + v;
            //cout << i << " " << v << "\n";
            if(cur % 2){
                if(i < k - 1){
                    ok = false;
                    break;
                }
                v++;
                ans++;
                if(i - k >= 0)a[i - k] -= 1;
            }
        }

        if(!ok){
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }
}

