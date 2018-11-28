#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <utility>
#include <queue>
#include <functional>
#include <stdint.h>

typedef int64_t ll;

using namespace std;

long double sol(vector<pair<int, int> > rhs, int K)
{
    const long double pi = acosl(-1);
    int N = rhs.size();
    long double res = 0;
    if(K == 1){
        for(int i = 0; i < N; i++){
            int R = rhs[i].first, H = rhs[i].second;
            res = max(res, 2*pi*R*H + pi*R*R);
        }
        return res;
    }
    //K >= 2
    sort(rhs.begin(), rhs.end());
    for(int b = N - 1; b >= 0; b--){
        long double R0 = rhs[b].first;
        int H0 = rhs[b].second;
        long double cur = pi*R0*R0;//top area decided by the bottom 
        cur += 2*pi*R0*H0;
        //max K - 1 H
        vector<ll> ps; //H*R
        if(b + 1 < K){
            break;
        }
        //b >= K - 1
        for(int i = b - 1; i >= 0; i--){
            int R = rhs[i].first, H = rhs[i].second;
            ps.push_back((ll)R*H);
        }
        sort(ps.begin(), ps.end());
        //max K - 1
        for(int i = b - 1; i >= 0; i--){
            cur += 2*pi*ps[i];
            if(b - i + 1 == K){ //K >= 2 (b - b + 1 + 1) = 2
                break;
            }
        }
        res = max(res, cur);
    }
    return res;
}
int main(int argc, char **argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(9);
    cout << fixed;
    int T;
    cin >> T; //1 100
    for(int cas = 1; cas <= T; cas ++){
        int N, K; //N 1 10/1e3 K 1 N
        cin >> N >> K;
        //Ri 1 1e6 hi 1 1e6
        vector<pair<int, int> > rhs(N);
        for(int i = 0; i < N; i++){
            cin >> rhs[i].first >> rhs[i].second;
        }
        cout << "Case #" << cas << ": " << sol(rhs, K) << endl;
    }
    return 0;
}
