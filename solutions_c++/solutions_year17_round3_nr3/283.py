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
    cin >> T;
    REP(tc, T){
        int N, K;
        double U;
        cin >> N >> K >> U;
        vector<double> P(N);
        REP(i, N)cin >> P[i];
        double lb = 0.0;
        double ub = 1.0;
        REP(_, 100){
            double mid = (lb+ub)/2.0;
            double sum = 0;
            REP(i, N){
                if(P[i]>mid)continue;
                sum += mid - P[i];
            }
            if(sum>U)ub = mid;
            else lb = mid;
        }
        double target = (lb+ub)/2;
        double res = 1.0;
        REP(i, N){
            if(target>P[i])P[i] = target;
            res *= P[i];
        }
        printf("Case #%d: %.6f\n", tc+1, res);
    }
    return 0;
}
