#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string.h>
using namespace std;
#define LL long long
const int MAX_N = 1002;
struct Pancake{
    double r, h;
    Pancake(int r=0, int h=0){
        this->r = r;
        this->h = h;
    }
};

const bool operator <(const Pancake &A, const Pancake &B){
    if(A.r==B.r){
        return A.h>B.h;
    }
    return A.r>B.r;
}

Pancake P[MAX_N];
double M[MAX_N][MAX_N];
int N, K;

double solve(int i, int k){
    if(M[i][k]!=-1){
        return M[i][k];
    }
    if(k==0){
        return M[i][k] = 0;
    }
    
    if((N-i)<k){
        return M[i][k] = -2;
    }
    
    double best = -2;
    for(int j=i; j<N; ++j){
        double opt = solve(j+1, k-1);
        if(opt<0){
            continue;
        }
        opt += 2.0*M_PI*P[j].r*P[j].h;
        if(k==K){
            opt += M_PI*P[j].r*P[j].r;
        }
        if(opt>best){
            best = opt;
        }
    }
    return M[i][k] = best;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t){
        scanf("%d%d", &N, &K);
        for(int i=0;i<N;++i){
            scanf("%lf%lf", &(P[i].r), &(P[i].h));
        }
        sort(P, P+N);
        for(int i=0;i<MAX_N;++i){
            for(int j=0;j<MAX_N;++j){
                M[i][j] = -1;
            }
        }
        double sol = solve(0, K);
        printf("Case #%d: %0.9lf\n", t, sol);
    }
    return 0;
}

