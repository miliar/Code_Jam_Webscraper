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

int T,D,N,k,s;

void solve(int cases) {
    scanf("%d%d",&D,&N);
    double max_t = -1.0;
    double max_v = -1;
    double max_k = -1;
    for(int i = 0 ; i < N ; i++ ) {
        scanf("%d%d",&k,&s);
        double t = 1.0*(D - k)/s;
        if(max_t < t) {
            max_t = t;
            max_v = s;
            max_k = k;
        }
    }
    double ans = 1.0 * D / max_t;
    printf("Case #%d: %.8f\n",cases,ans);
}

int main() {
    scanf("%d",&T);
    for(int t = 1 ; t <= T ;t++) solve(t);
    return 0;
}
