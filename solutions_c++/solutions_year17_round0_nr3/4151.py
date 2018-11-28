#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;
typedef unsigned long long LLU;
typedef pair<LLU, LLU> PAIR;
typedef pair<LLU,  PAIR> DS;

int T;
LLU n, k;


int main() {
    scanf("%d",&T);
    for(int TC = 1; TC<=T; TC++){
        scanf("%llu%llu",&n,&k);
        //printf(">> %llu %llu\n",n,k);

        priority_queue<DS> pq;
        pq.push(DS(n,PAIR(1,n)));
        DS temp;
        LLU mid = 0;
        for(LLU i = 0; i<k; i++){
            temp = pq.top();
            pq.pop();
            mid = (temp.second.first) + ((temp.second.second - temp.second.first) / 2);
            pq.push(DS(mid - temp.second.first,PAIR(temp.second.first, mid - 1)));
            pq.push(DS(temp.second.second - mid, PAIR(mid + 1, temp.second.second)));
        }
        LLU left = mid - temp.second.first, right = temp.second.second - mid;
        LLU MAX = max(left,right), MIN = min(left,right);
        printf("Case #%d: %lld %lld\n",TC,MAX,MIN);
        //printf("Case #%d: %lld %lld\n",TC,n,k);
    }
    return 0;
}
/*
5
4 2
5 2
6 2
1000 1000
1000 1
 */