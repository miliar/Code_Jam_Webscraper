#include <iostream>
using namespace std;

int dp[101][101][101];

int doit(int P, int sum, int x[4]) {
    int& ret=dp[x[1]][x[2]][x[3]];
    if(ret+1) return ret;
    ret = 0;
    for(int i=1; i<P; i++)
        if(x[i]>0) {
            x[i]--;
            ret=max(ret, doit(P, (sum+i)%P, x));
            x[i]++;
        }
    ret += (sum==0);
    return ret;
}

int main(void) {
    int T; cin >> T;
    for(int ts=1; ts<=T; ts++) {
        int N, P; cin >> N >> P;
        int cnt[4] = {0, 0, 0, 0};
        memset(dp, -1, sizeof(dp));
        dp[0][0][0]=0;
        for(int i=0; i<N; i++) {
            int x; cin >> x;
            cnt[x%P]++;
        }
        int ret = cnt[0] + doit(P, 0, cnt);
        cout << "Case #" << ts << ": " << ret << endl;
    }
}
