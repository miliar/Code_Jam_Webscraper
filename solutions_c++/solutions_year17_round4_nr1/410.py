#include <bits/stdc++.h>

using namespace std;

int ct[4];

int main()
{
    freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int cnt = 0; cnt < t; cnt++){
        int n, p;
        cin >> n >> p;
        for (int i = 0; i < p; i++){
            ct[i] = 0;
        }
        for (int i = 0; i < n; i++){
            int a;
            cin >> a;
            ct[a % p]++;
        }
        int ans = 0;
        ans += ct[0];
        if (p == 2){
            ans += (ct[1] + 1) / 2;
        }
        else if (p == 3){
            int x = min(ct[1], ct[2]);
            int y = max(ct[1], ct[2]) - x;
            ans += x;
            ans += (y + 2) / 3;
        }
        else{
            ans += ct[2] / 2;
            ct[2] &= 1;
            int x = min(ct[1], ct[3]);
            int y = max(ct[1], ct[3]) - x;
            ans += x;
            if (ct[2] && y >= 2){
                ans++;
                ct[2] = 0;
                y -= 2;
            }
            ans += y / 4;
            y = y & 3;
            if (ct[2] || y){
                ans++;
            }
        }
        cout << "Case #" << cnt + 1 << ": " << ans << "\n";
    }
    return 0;
}
