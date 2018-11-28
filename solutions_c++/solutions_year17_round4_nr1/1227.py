#include <bits/stdc++.h>
#define x first
#define y seconde
#define all(a) a.begin(), a.end()
#define mp make_pair
#define pub push_back
#define ll long long

using namespace std;

int tt;
int n, p;
int kol[7];
int was[7];
int a[10007];

int get(int k1, int k2, int k3){
    for (int i = 1; i <= 3; i++) was[i] = kol[i];
    was[1] -= k1; was[3] -= k1;
    was[1] -= 2 * k2; was[2] -= k2;
    was[2] -= k3; was[3] -= 2 * k3;
    int ans = k1 + k2 + k3;
    bool f = 0;
    for (int i = 1; i <= 3; i++){
        if (was[i] < 0) return 0;
    }
    ans += was[1] / 4;
    if (was[1] % 4 != 0) f = 1;
    ans += was[2] / 2;
    if (was[2] % 2 != 0) f = 1;
    ans += was[3] / 4;
    if (was[3] % 4 != 0) f = 1;
    ans += f;
    return ans;
}

int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    cin >> tt;
    for (int ss = 1; ss <= tt; ss++){
        cin >> n >> p;
        memset(kol, 0, sizeof(kol));
        for (int i = 0; i < n; i++) cin >> a[i];
        for (int i = 0; i < n; i++) kol[a[i] % p]++;
        if (p == 2){
            int ans = 0;
            ans += kol[0];
            ans += (kol[1] + 1) / 2;
            cout << "Case #" << ss << ": " << ans << endl;
        } else if (p == 3) {
            int ans = 0;
            ans += kol[0];
            int k = min(kol[1], kol[2]);
            ans += k;
            kol[1] -= k, kol[2] -= k;
            if (kol[1] > 0){
                ans += kol[1] / 3;
                if (kol[1] % 3 != 0) ans++;
            }
            if (kol[2] > 0){
                ans += kol[2] / 3;
                if (kol[2] % 3 != 0) ans++;
            }
            cout << "Case #" << ss << ": " << ans << endl;
        } else {
            int ans = 0;
            for (int i = 0; i < 101; i++){
                for (int j = 0; j < 101; j++){
                    for (int s = 0; s < 101; s++){
                        ans = max(ans, get(i, j, s));
                    }
                }
            }
            ans += kol[0];
            cout << "Case #" << ss << ": " << ans << endl;
        }
    }
    return 0;
}
