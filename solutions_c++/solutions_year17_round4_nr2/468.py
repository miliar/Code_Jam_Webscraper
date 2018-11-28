
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std ; 

typedef long long ll ; 

vector<int> cust[1111] ; 
int N, C, M ; 

int stat[1111] = {0} ; 
int promCnt ; 

vector<pair<int, int>> whoBuy[1111] ; 
int cusMoveCnt[1111] ; 

bool ok(int nt) {
    for(int i = 1 ; i <= C ; i++)
        if(cust[i].size() > nt)
            return false ; 
    memset(stat, 0, sizeof(stat)) ; 
    for(int i = 1 ; i <= N ; i++)
        whoBuy[i].clear() ; 
    for(int i = 1 ; i <= C ; i++)
        for(int p: cust[i]) {
            stat[p]++ ; 
            whoBuy[p].push_back({cust[i].size(), i}) ; 
        }
    int sum = 0 ; 
    for(int i = 1 ; i <= N ; i++) {
        sum += stat[i] ; 
        if(sum > i*nt)
            return false ; 
    }
    for(int i = 1 ; i <= N ; i++)   
        sort(whoBuy[i].begin(), whoBuy[i].end()) ; 
    promCnt = 0 ; 
    memset(cusMoveCnt, 0, sizeof(cusMoveCnt)) ; 
    int priorEmp = 0 ; 
    for(int i = 1 ; i <= N ; i++) { 
        int exc = stat[i]-nt ; 
        assert(whoBuy[i].size() == stat[i]) ; 
        if(exc > 0) {
            promCnt += exc ; 
            if(priorEmp < exc)
                return false ; 
        }
        /*
        for(int j = 0 ; j < exc ; j++) {
            cusMoveCnt[whoBuy[i][j].first]++ ; 
        }*/
        priorEmp += nt-stat[i] ; 
    }
    for(int i = 1 ; i <= C ; i++)
        if(cust[i].size() + cusMoveCnt[i] > nt)
            return false ;
    return true ; 
}


void sol(){
    scanf("%d%d%d", &N, &C, &M) ; 
    for(int i = 1 ; i <= C ; i++)
        cust[i].clear() ; 
    for(int i = 0 ; i != M ; i++) {
        int P, B ; 
        scanf("%d%d", &P, &B) ; 
        cust[B].push_back(P) ; 
    }
    int lb = 0, ub = 1000 ; 
    while(lb + 1 < ub) {
        int mid = (lb+ub)/2 ; 
        if(ok(mid))
            ub = mid ; 
        else
            lb = mid ; 
    }
    assert(ok(ub)) ; 
    printf("%d %d\n", ub, promCnt) ; 
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


