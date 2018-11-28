#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
long dp[4][101][101][101];
long p = -1;
long go(long mod, long a, long b, long c){
    if(a+b+c==0){
        return 0;
    }
    if(dp[mod][a][b][c]!=-1){
        return dp[mod][a][b][c];
    }
    long ret = 0;
    long add = 0;
    if(mod==0){
        add = 1;
    }
    if(a>0){
        ret = max(ret,go((1+mod)%p,a-1,b,c));
    }
    if(b>0){
        ret = max(ret,go((2+mod)%p,a,b-1,c));
    }
    if(c>0){
        ret = max(ret,go((3+mod)%p,a,b,c-1));
    }
    ret = ret+add;
    dp[mod][a][b][c] = ret;
    return ret;
}
int main() {
    ifstream in ("cjA17.in");
    ofstream out ("cjA17.out");
    
    long cases;
    in >> cases;
    for(long q=1; q<=cases; q++){
        long n;
        in >> n >> p;
        long val[4];
        val[0] = 0;
        val[1] = 0;
        val[2] = 0;
        val[3] = 0;
        for(long i = 0; i<n; i++){
            long x;
            in >> x;
            val[x%p]++;
        }
        for(long a = 0; a<4; a++){
            for(long b = 0; b<=n; b++){
                for(long c = 0; c<=n; c++){
                    for(long d = 0; d<=n; d++){
                        dp[a][b][c][d] = -1;
                    }
                }
            }
        }
        long ans = val[0]+go(0,val[1],val[2],val[3]);
        out << "Case #" << q << ": " << ans << endl;
    }
    
    return 0;
}