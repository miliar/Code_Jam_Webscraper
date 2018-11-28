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

#define EPS 1e-8

const double PI = acos(-1.0);

int N,K;
pair<int,int> p[1111];
double f[1111][1111];


void solve(int cases) {
    scanf("%d%d",&N,&K);
    for(int i = 1 ; i <= N; i++ ) {
        scanf("%d%d",&p[i].first,&p[i].second);
    }
    sort(p+1,p+N+1,greater<pair<int,int> >());
    memset(f,0,sizeof(f));
    for(int i = 1 ; i <= N ; i++ ) {
        for(int j = 1 ; j <= K ; j++ ) if(i>=j) {
            if(f[i-1][j-1] < EPS) {
                f[i][j] = max(PI*p[i].first*p[i].first+2*PI*p[i].first*p[i].second,f[i-1][j]);
            } else {
                f[i][j] = max(f[i-1][j-1]+2*PI*p[i].first*p[i].second,f[i-1][j]);
            }
            //printf("%.6f ",f[i][j]);
        }
        //printf("\n");
    }
    printf("Case #%d: %.8f\n",cases,f[N][K]);
}


int main() {
    int T;
    scanf("%d",&T);
    for(int t = 1 ; t<=T; t++) solve(t);
    return 0;
}
