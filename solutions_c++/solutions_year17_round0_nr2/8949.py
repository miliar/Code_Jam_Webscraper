#include <bits/stdc++.h>
using namespace std;



int main(){
    ios_base::sync_with_stdio(false);
    freopen("in", "r", stdin); freopen("out", "w", stdout);
    int t; cin >> t;
    for(int tt = 0 ; tt < t; ++tt){
        long long N; cin >> N;
        int dec[18];
        for(int i = 0 ; i < 18; ++i){
            dec[17-i] = N % 10;
            N /= 10;
        }
        int cur = dec[17];
        for(int i = 0 ; i < 18; ++i){
            if(dec[17-i] <= cur) cur = dec[17 - i];
            else{
                for(int j = 18-i ; j < 18; ++j){
                    dec[j] = 9;
                }
                --dec[17-i]; cur = dec[17-i];
            }
        }
        long long ans = 0;
        for(int i = 0 ; i < 18; ++i){
            ans *= 10; ans += dec[i];
        }
        cout << "Case #" << tt + 1 << ": " << ans << endl;
    }
    return 0;
}


