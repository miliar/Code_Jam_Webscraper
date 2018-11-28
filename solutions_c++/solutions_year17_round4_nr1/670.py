#include <bits/stdc++.h>

using namespace std;

int n,p;
int cnt1,cnt2,cnt3;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++){
        cin >> n >> p;
        int ans = 0;
        cnt1=0;cnt2=0;cnt3=0;
        for (int i = 0; i < n; i++){
            int num;
            cin >> num;
            if (num % p == 0){
                ans++;
            }
            else if (num % p == 1)
                cnt1++;
            else if (num % p == 2)
                cnt2++;
            else if (num % p == 3)
                cnt3++;
            else{
                int a = 0;
                cout << 3 / a;
            }
        }
        if (p==2){
            ans += cnt1 / 2;
            cnt1 %= 2;
            if (cnt1 >= 1)
                ans++;
        }
        else if (p==3){
            int mini = min(cnt1, cnt2);
            ans += mini;
            int k = cnt1+cnt2-2*mini;
            ans += k/3;
            k %=3;
            if (k >=1){
                ans++;
            }
        }
        if (p==4){
            ans += cnt2 / 2;
            cnt2 %= 2;
            int mini = min(cnt1, cnt3);
            ans += mini;
            int k = cnt1 + cnt3 - 2 * mini;
            ans += k / 4;
            k %=4;
            if (k >= 2 && cnt2 >= 1){
                ans++;
                k -= 2; cnt2--;
            }
            if (k || cnt2)
                ans++;
        }
        cout << "Case #" << test << ": " << ans << "\n";
    }
    return 0;
}
