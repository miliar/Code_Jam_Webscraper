#include<iostream>
#include<cstdint>
#include<cassert>
#define MAX 1005

using namespace std;
typedef int64_t var;
var t, n, q;

var E[MAX];
var S[MAX];
var nextD[MAX];
double timeTaken[MAX];
double dp[MAX][MAX];

int main(){
    cin >> t;
    for(var _t = 1; _t <= t; ++_t){
        cin >> n >> q;
        assert(q==1);
        for(var i = 1; i <= n; ++i){
            cin >> E[i] >> S[i];
        }
        for(var i = 1; i <= n; ++i){
            for(var j = 1; j <= n; ++j){
                var buf;
                cin >> buf;
                assert(buf==-1||j==i+1);
                if(buf!=-1) nextD[i]=buf;
                dp[i][j]=0.0f;
            }
        }
        for(var i = 1; i <= q; ++i){
            var a, b;
            cin >> a >> b;
            assert((a==1)&&(b==n));
        }
        timeTaken[n]=0.0f;
        //dp[n-1][n]=((double)nextD[n-1])/S[n-1];
        //timeTaken[n-1]=dp[n-1][n];
        for(var i = n-1; i > 0; --i){
            var maxDist = E[i];
            var distTaken = nextD[i];
            timeTaken[i]=9999999999999.0f;
            for(var j = i+1; j<=n && distTaken <= maxDist; ++j){
                dp[i][j]=((double)distTaken)/S[i]+timeTaken[j];
                timeTaken[i]=min(timeTaken[i],dp[i][j]);
                distTaken+=nextD[j];
            }
        }
        printf("Case #%lu: %lf\n", _t, timeTaken[1]);
    }
    return 0;
}
