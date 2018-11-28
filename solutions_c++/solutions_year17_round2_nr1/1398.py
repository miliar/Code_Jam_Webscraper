#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

int main(){
    int T;
    scanf("%d", &T);
    REP(tc, T){
        int D, N;
        scanf("%d %d", &D, &N);
        double max_time = 0;
        REP(i, N){
            int K, S;
            scanf("%d %d", &K, &S);
            double rem = D-K;
            max_time = max(max_time, rem/S);
        }
        double res = D / max_time;
        printf("Case #%d: %.9f\n", tc+1, res);
    }
    return 0;
}
