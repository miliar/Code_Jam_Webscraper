#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int main(){
    int T, D, N, K, S;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> D >> N;
        double ans = 0;
        for(int i = 0; i < N; i++) {
            cin >> K >> S;
            ans = max(ans, ((double)(D - K))/S);
        }
        printf("Case #%d: %.7f\n", t, ((double)D)/ans);
    }
    return 0;
}
