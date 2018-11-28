#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;
const ll MOD = 1000000007;

int solve(){
    string S;
    int K;
    cin >> S >> K;
    int n = S.size();
    int ret = 0;
    for(int i=0;i<n;i++){
        if(S[i] == '-'){
            if(n <= i+K-1) return -1;
            ret++;
            for(int j=0;j<K;j++){
                if(S[i+j] == '+') S[i+j] = '-';
                else S[i+j] = '+';
            }
        }
    }
    return ret;
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int res = solve();
        printf("Case #%d: ", t);
        if(res >= 0) cout << res << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}