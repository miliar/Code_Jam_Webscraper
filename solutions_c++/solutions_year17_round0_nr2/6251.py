#include <bits/stdc++.h>

using namespace std;
 

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int o = 1; o <= T; o++){
        cout << "Case #" << o << ": ";
        long long N;
        cin >> N;
        if (N == 1000000000000000000LL){
            cout << 999999999999999999LL << endl;
            continue;
        }
        if (N < 10){
            cout << N << endl;
            continue;
        }
        long long M = N;
        int l = 0;
        while (M > 0){
            M /= 10;
            l++;
        }
        long long r = 0;
        long long ans = 0;
        for (int i = 0; i < l-1; i++)
            ans = ans*10+9;

        for (int i = 0; i < l; i++)
            r = r*10 + 1;

        if (N < r){
            cout << ans << endl;
            continue;
        }else
            ans = r;

        for (int i = l; i >= 0; i--){
            for (int j = 2; j <= 9; j++){
                long long s = r;
                long long p = 1LL;
                for (int k = 0; k < i; k++){
                    s -= (s/p)%10*p;
                    s += j*p;
                    p *= 10;
                }
                if (s <= N){
                    ans = s;
                    r = ans;
                }
            }
        }
        cout << ans << endl;
    }   
    return 0;
}