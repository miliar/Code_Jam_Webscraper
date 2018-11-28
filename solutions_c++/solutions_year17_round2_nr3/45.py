//#include {{{
#include <iostream>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <bitset>
#include <vector>
#include <complex>
#include <algorithm>
using namespace std;
// }}}
// #define {{{
typedef long long ll;
typedef double db;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define de(x) cout << #x << "=" << x << endl
#define rep(i,a,b) for(int i=a;i<(b);++i)
#define per(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
// }}}

const int N = 101;
const ll linf = 1ll<<50;
int T , n , E[N] , S[N];
ll D[N][N];
double dis[N][N];


int main(){
    int T;
    scanf("%d",&T);
    rep(i,0,T){
        cerr << i << endl;
        int n , Q;
        scanf("%d%d",&n,&Q);
        rep(i,0,n) scanf("%d%d",E + i,S + i);
        rep(i,0,n) rep(j,0,n) scanf("%lld",D[i] + j);
        rep(i,0,n) rep(j,0,n) if(D[i][j] == -1) D[i][j] = linf;
        rep(i,0,n) D[i][i] = 0;
        rep(k,0,n) rep(i,0,n) rep(j,0,n) D[i][j] = min(D[i][j] , D[i][k] + D[k][j]);
        //rep(i,0,n) rep(j,0,n) printf("%lld%c",D[i][j]," \n"[j+1==n]);
        rep(i,0,n) rep(j,0,n)
            if(D[i][j] <= E[i]) dis[i][j] = 1. * D[i][j] / S[i];
            else dis[i][j] = 1e50;
        //rep(i,0,n) rep(j,0,n) printf("%f%c",dis[i][j]," \n"[j+1==n]);
        rep(k,0,n) rep(i,0,n) rep(j,0,n) dis[i][j] = min(dis[i][j] , dis[i][k] + dis[k][j]);
        printf("Case #%d:",i + 1);
        rep(i,0,Q){
            int s , t;
            scanf("%d%d",&s,&t);
            --s;--t;
            printf(" %.16f",dis[s][t]);
        }
        printf("\n");
    }
    return 0;
}
