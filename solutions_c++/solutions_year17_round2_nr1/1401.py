#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>

using namespace std;
typedef long long LL;

double solve(LL D, LL N, vector<pair<LL,LL> >& horses){
    double res = 0;
    for(LL i = 0; i < N; ++i){
        double t = (double)(D - horses[i].first) / horses[i].second;
        res = max(res, t);
    }
    return D / res;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        LL D, N;
        cin >> D >> N;
        vector<pair<LL,LL> > horses(N);
        for(int i = 0; i < N; ++i){
            cin >> horses[i].first >> horses[i].second;
        }
        double res = solve(D, N, horses);
        printf("Case #%d: %.11f\n", t, res);
    }
    return 0;
}

