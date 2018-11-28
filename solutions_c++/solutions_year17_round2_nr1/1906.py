#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
#define LL long long
const int MAX_N=1001;

struct Horse{
    LL k, s;
    Horse(LL k, LL s){
        this->k = k;
        this->s = s;
    }
    
};
const bool operator<(const Horse &A, const Horse &B){
    return A.k<B.k;
}


double solve(LL D, LL N, vector<Horse> &H){
    sort(H.begin(), H.end());
    double t = double(D - H[N-1].k)/H[N-1].s;
    for(int i=N-2; i>=0; --i){
        double tt = double(D - H[i].k)/H[i].s;
        if(tt>t){
            t = tt;
        }
    }
    double target = D/t;
    return target;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t){
        vector<Horse> H;
        int D, N;
        scanf("%d%d", &D, &N);
        for(int i=0;i<N;++i){
            int k,s;
            scanf("%d%d", &k, &s);
            H.push_back(Horse(k, s));
        }
        double sol = solve(D, N, H);
        printf("Case #%d: %0.6lf\n", t, sol);
    }
    return 0;
}

