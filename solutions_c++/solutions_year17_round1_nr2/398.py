
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cassert>

using namespace std ; 

typedef long long ll ; 

int R[55];

vector<int> start[2222222];
vector<int> close[2222222];

pair<int, int> findItv(int q, int r) {
    int rat = q/r;
    int i = rat ; 
    while(q*10 <= r*i*11)
        i--;
    int lb = i+1 ; 
    int ub = i ;
    while(r*(ub+1)*9 <= q*10)
        ub++;
    if(ub >= lb){
        assert(!(r*(lb-1)*9 <= q*10 && q*10 <= r*(lb-1)*11));
        assert(  r* lb   *9 <= q*10 && q*10 <= r*lb*11);
        assert(!(r*(ub+1)*9 <= q*10 && q*10 <= r*(ub+1)*11));
        assert(  r* ub   *9 <= q*10 && q*10 <= r*ub*11);
    }
    else {
        assert(!(r*(ub)*9 <= q*10 && q*10 <= r*(ub)*11));
        assert(!(r*(lb)*9 <= q*10 && q*10 <= r*(lb)*11));
    }
    return {lb, ub};
}

void sol(){
    int N, P ; 
    scanf("%d%d", &N, &P) ; 
    for(int i = 0 ; i != N ; i++)
        scanf("%d", R+i) ; 
    for(int i = 0 ; i != 2222222 ; i++) {
        start[i].clear();
        close[i].clear();
    }
    for(int i = 0 ; i != N ; i++) {
        for(int j = 0 ; j != P ; j++) {
            int q ; 
            scanf("%d", &q);
            auto p = findItv(q, R[i]);
//            fprintf(stderr, "itv=(%d, %d)\n", p.first, p.second);
            if(p.first == 0)
                p.first = 1;
            if(p.second - p.first >= 0) {
                assert(p.first > 0);
        //        if(p.second >= 2222222) {
      //              printf("q = %d, R[i] = %d\n", q, R[i]);
    //            }
                assert(p.second < 2222222);
                start[p.first].push_back(i);
                close[p.second].push_back(i);
            }
        }
    }
    int stat[55] = {0};
    int used[55] = {0};
    int ans = 0 ;
    for(int i = 1 ; i != 2222222 ; i++) {
        for(auto s: start[i]) 
            stat[s]++;
        int minv = 1e+8 ;
        for(int s = 0 ; s != N ; s++) 
            minv = min(minv, stat[s]);
        assert(minv >= 0);
        if(minv > 0) {
            for(int s = 0 ; s != N ; s++) {
                stat[s] -= minv;
                used[s] += minv ; 
            }
            ans += minv;
        }
        for(auto c: close[i]) {
            if(used[c])
                used[c]--;
            else
                stat[c]--;
            assert(stat[c] >= 0);
        }
    }
    printf("%d\n", ans);
}

int main()
{
    int T ; 
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        fprintf(stderr, "solving case (%d / %d)...\n", time, T) ; 
        printf("Case #%d: ", time) ; 
        sol() ; 
    }
    return 0 ; 
}


