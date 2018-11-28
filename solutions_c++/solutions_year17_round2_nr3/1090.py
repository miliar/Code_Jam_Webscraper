#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <complex>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

const int MAX_N = 111;

int T;
int N,Q;
int E[MAX_N],S[MAX_N],D[MAX_N][MAX_N];
int U[MAX_N],V[MAX_N];

double dfs(int n,int d,int v) {
    //printf("[dfs: n = %d,d = %d,v = %d]:\n",n,d,v);
    double res = 0;
    if( n == N - 1 ) return res;
    if(D[n][n+1] > d) {
        res = res + 1.0 * D[n][n+1] / S[n] + dfs(n+1,E[n]-D[n][n+1],S[n]);
    } else {
        double r1 = 1.0 * D[n][n+1] / v + dfs(n+1,d-D[n][n+1],v);
        
        double r2 = 1.0 * D[n][n+1] / S[n] + dfs(n+1,E[n]-D[n][n+1],S[n]);
        //printf("r1 = %.9f, r2 = %.9f\n",r1,r2);
        res = res + min(r1,r2);
    }
    return res;
}

void solve(int cases) {
    scanf("%d%d",&N,&Q);
    for(int i = 0 ; i < N ; i++ ) {
        scanf("%d%d",&E[i],&S[i]);
    }
    for(int i = 0 ; i < N ; i++ ) {
        for(int j = 0 ; j < N ; j++ ) {
            scanf("%d",&D[i][j]);
        }
    }
    for(int i = 0 ; i < Q ;i ++ ) {
        scanf("%d%d",&U[i],&V[i]);
    }
    double res = 1.0 * D[0][1] / S[0] + dfs(1,E[0]-D[0][1],S[0]);
    printf("Case #%d: %.8f\n",cases,res);
}

int main() {
    scanf("%d",&T);
    for(int t = 1 ; t<=T; t++) solve(t);
    return 0;
}
