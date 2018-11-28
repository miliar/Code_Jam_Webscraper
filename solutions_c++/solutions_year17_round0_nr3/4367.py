#include <cstdio>
#include <cmath>
#include <stack>
#include <utility>
#include <queue>
using namespace std;
pair<int,int> f(double n){
    double k = floor(n/2);
    return make_pair(n - k, k);
}
pair<int,int> rcsf(priority_queue<int>& pq,int& x,const int& dlv,int lv = 0){
    if(lv == dlv){
        int cidx = 1 << (int)log2(x);
        for(int i = 1; i < cidx; i++){
            pq.pop();
        }
        return f(pq.top());
    }
    priority_queue<int> now;
    pair<int,int> an;
    while(!pq.empty()){
        an = f(pq.top());
        now.push(an.first);
        now.push(an.second);
    }
    return rcsf(now,x,dlv,lv+1);
}
int main(){
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    int n,k,h;
    for(int i = 1; i <= t; i++){
        scanf("%d%d",&n,&k);
        priority_queue<int> pq;
        pq.push(n);
        for(int j = 1; j < k; j++){
            h = pq.top()-1;
            pq.pop();
            pq.push(h/2);
            pq.push(h - h/2);
        }
        pair<int,int> ans = f(pq.top() - 1);
        printf("Case #%d: %d %d\n",i,ans.first,ans.second);
    }
    return 0;
}
/// O.O.O.O.OO
/** 8 1 -> 4 3
    8 2 -> 2 1
    8 3 -> 1 1
    8 4 -> 1 0
    8 5 -> 0 0
    8 6 -> 0 0
    8 7 -> 0 0
    8 8 -> 0 0

    OOO.OO
    4 1 -> 2 1
    4 2 -> 1 0
    4 3 -> 0 0
    4 4 -> 0 0

    O.OOO.O
    5 1 -> 2 2
    5 2 -> 1 0
    5 3 -> 1 0
    5 4 -> 0 0
    5 5 -> 0 0

    O.OO.O.O
    6 1 -> 3 2
    6 2 -> 1 1
    6 3 -> 1 0
    6 4 -> 0 0
    6 5 -> 0 0
    6 6 -> 0 0

    O.O.O.O.O
    7 1 -> 3 3
    7 2 -> 1 1
    7 3 -> 1 1
**/
