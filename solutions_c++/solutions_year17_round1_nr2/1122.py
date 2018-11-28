#include <bits/stdc++.h>

using namespace std;

int r[51];

pair <int, int> range(int x, int y){
    pair <int, int> ans = make_pair(-1, -1);
    int left, ll;
    if (x % 11 == 0) left = (x * 10 / 11); else left = x * 10 / 11 + 1;
    int right, rr;
    if (x % 9 == 0) right = x * 10 / 9; else right = x * 10 / 9;

    if (left % y == 0){
        ll = left / y;
    } else ll = (left / y) + 1;
    
    if (right % y == 0){
        rr = right / y;
    } else rr = right / y;
    
    if (ll <= rr) ans = make_pair(ll, rr);
    return ans;
}

int main(){
    long long i,j,k,l,m,n,test,t, p;
    cin >> test;
    for (t = 0; t < test; t++){
        cin >> n >> p;
        cout << "Case #" << t + 1 << ": ";
        for (i = 0; i < n; i++){
            cin >> r[i];
        }
        vector <int> a[n];
        for (i = 0; i < n; i++){
            for (j = 0; j < p; j++){
                cin >> l;
                a[i].push_back(l);
            }
            sort(a[i].begin(), a[i].end());
        }
        int ans = 0;
        if (n == 1){
            for (i = 0; i < p; i++){
                if (range(a[0][i], r[0]).first != -1){
                    ans++;
                }
            }
            cout << ans << "\n";
        } else
        {
            for (int mask1 = 0; mask1 < (1 << p); mask1 ++){
                for (int mask2 = 0; mask2 < (1 << p); mask2 ++){
                    int bits1 = 0, bits2 = 0;
                    for (i = 0; i < p; i++){
                        if (mask1 & (1<<i)) bits1 ++;
                        if (mask2 & (1<<i)) bits2 ++;
                    }
                    if (bits1 == bits2 && bits1 > 0){
                        int p1 = -1,  p2 = -1;
                        int cur = 0;
                        for (i = 0; i < bits1; i++){
                            
                            for (p1 = p1 + 1; p1 < p; p1++){
                                if (mask1 & (1 << p1)){
                                    break;
                                }
                            }
                            for (p2 = p2 + 1; p2 < p; p2++){
                                if (mask2 & (1 << p2)){
                                    break;
                                }
                            }

                            pair <int, int> rng1 = range(a[0][p1], r[0]);
                            pair <int, int> rng2 = range(a[1][p2], r[1]);
                            //cout << a[0][p1] << " " << r[0] << "         " << rng1.first << " " << rng1.second << "\n";
                            //cout << a[1][p2] << " " << r[1] << "         " << rng2.first << " " << rng2.second << "\n";
                            if (rng1.first >= 0 && rng2.first >= 0){
                                if (
                                    (rng1.first >= rng2.first && rng1.first <= rng2.second) ||
                                    (rng1.second >= rng2.first && rng1.second <= rng2.second) ||
                                    (rng2.first >= rng1.first && rng2.first <= rng1.second) ||
                                    (rng2.second >= rng1.first && rng2.second <= rng1.second)
                                   ){
                                        cur++;
                                   }
                            }
                                                                                    
                        }
                        if (cur > ans) ans = cur;   
                    }
                }
            }
            cout << ans << "\n";
        }
    }
    return 0;
}
