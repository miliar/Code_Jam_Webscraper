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

int N, P;
map<pair<int, vector<int> >, int> memo;

int rec(int now, vector<int> &mod){
    bool last = true;
    REP(i, mod.size()){
        if(mod[i]>0)last = false;
    }
    if(last){
        return 0;
    }
    pair<int, vector<int> > key = make_pair(now, mod);
    if(memo.count(key)>0)return memo[key];
    int res = 0;
    REP(i, mod.size()){
        if(mod[i]==0)continue;
        int next = (now + i) % P;
        mod[i]--;
        res = max(res, rec(next, mod));
        mod[i]++;
    }
    if(now==0)res++;
    memo[key] = res;
    return res;
}

int main(){
    int T;
    cin >> T;
    memo = map<pair<int, vector<int> >, int>();
    REP(tc, T){
        cin >> N >> P;
        vector<int> mod(P, 0);
        REP(i, N){
            int g;
            cin >> g;
            mod[g%P]++;
        }
        int res = rec(0, mod);
        printf("Case #%d: %d\n", tc+1, res);
    }
    return 0;
}
