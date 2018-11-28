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

LL solve(){
    LL N, K;
    cin >> N >> K;
    priority_queue<LL> que;
    map<LL, LL> memo;
    memo[N] = 1;
    que.push(N);
    LL searched = 0;
    while(!que.empty()){
        LL now = que.top();que.pop();
        LL cnt = memo[now];
        if(searched < K && K <= searched + cnt){
            return now;
        }
        searched += cnt;
        LL left = now / 2;
        LL right = (now - 1LL) / 2;
        if(memo.count(left)==0){
            memo[left] = 0;
            que.push(left);
        }
        if(memo.count(right)==0){
            memo[right] = 0;
            que.push(right);
        }
        memo[left] += cnt;
        memo[right] += cnt;
    }
    return 1LL;
}

int main(){
    int T;
    cin >> T;
    REP(tc, T){
        LL res = solve();
        LL left = res / 2;
        LL right = (res - 1LL) / 2;
        cout << "Case #" << tc+1 << ": " << left << " " << right << endl;
    }
    return 0;
}
