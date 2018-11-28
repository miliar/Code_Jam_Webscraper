#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
#define MIN(a, b) (((a)<(b))?(a):(b))
#define MAX(a, b) (((a)>(b))?(a):(b))

struct Stall{
    int i, m, M;
    Stall(int i=-1, int l=0, int r=0){
        this->i = i;
        m = MIN(l, r);
        M = MAX(l, r);
    }
};

struct Interval{
    int first, len;
    Interval(int first, int len){
        this->first = first;
        this->len = len;
    }
};

const bool operator<(const Interval &A, const Interval &B){
    if(A.len == B.len){
        return A.first < B.first;
    }
    return A.len > B.len;
}

Stall select_stall(const Interval &I){
    if(I.len==1){
        return Stall(I.first, 0, 0);
    }else if(I.len==2){
        return Stall(I.first, 0, 1);
    }
    
    if(I.len%2 == 1){
        int m = (I.len-1)/2;
        return Stall(I.first + m, m, m);
    }else{
        int m = I.len/2;
        return Stall(I.first + m - 1, m-1, m);
    }
}

Stall solve_medium(int n, int k){
    set<Interval> S;
    S.insert(Interval(1, n));
    Stall last;
    for(int j=1;j<=k;++j){
        Interval I = *(S.begin());
        S.erase(S.begin());
        Stall sel = select_stall(I);
        if(j==k){
            return sel;
        }else{
            Interval left(I.first, sel.i - I.first);
            Interval right(sel.i + 1, I.first + I.len -1 - sel.i);
            if(left.len>0){
                S.insert(left);
            }
            if(right.len>0){
                S.insert(right);
            }
        }
    }
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; ++t){
        int n, k;
        scanf("%d%d", &n, &k);
        Stall sol = solve_medium(n, k);
        printf("Case #%d: %d %d\n", t, sol.M, sol.m);
    }
    return 0;
}

