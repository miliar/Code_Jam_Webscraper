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

const int INF = 1<<28;

int memo[2][24*60][721][2];

int rec(int c, int t, int ct, const vector<int> &C, const vector<int> &J, const int start){
    if(t==24*60){
        if(c==0 && C[0])return INF;
        if(c==1 && J[0])return INF;
        if(ct==720)return abs(c-start);
        return INF;
    }
    if(ct>720 || t-ct>720)return INF;
    if(memo[c][t][ct][start]!=-1)return memo[c][t][ct][start];
    int res = INF;
    if(c==0){// cameron
        if(C[t])return INF;
        res = min(res, rec(c, t+1, ct+1, C, J, start));
        res = min(res, rec(1-c, t+1, ct, C, J, start) + 1);
    } else {// jamie
        if(J[t])return INF;
        res = min(res, rec(c, t+1, ct, C, J, start));
        res = min(res, rec(1-c, t+1, ct+1, C, J, start) + 1);
    }
    memo[c][t][ct][start] = res;
    return res;
}

int main(){
    int T;
    cin >> T;
    REP(tc, T){
        int AC, AJ;
        cin >> AC >> AJ;
        vector<int> C(24*60+1, 0);
        vector<int> J(24*60+1, 0);
        REP(i, AC){
            int c, d;
            cin >> c >> d;
            for(int j=c; j<d; j++)C[j] = 1;
        }
        REP(i, AJ){
            int c, d;
            cin >> c >> d;
            for(int j=c; j<d; j++)J[j] = 1;
        }
        memset(memo, -1, sizeof(memo));
        int cstart = rec(0, 0, 0, C, J, 0);
        int jstart = rec(1, 0, 0, C, J, 1);
        //cerr << cstart << " " << jstart << endl;
        int res = min(cstart, jstart);
        printf("Case #%d: %d\n", tc+1, res);
    }
    return 0;
}
