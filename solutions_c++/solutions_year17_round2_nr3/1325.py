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

int N, Q;
vector<int> E;
vector<int> S;
vector<vector<int> > D;
map<pair<int, int>, double> memo;
const double EPS = 1e-9;

double rec(int pos, int use){
    if(pos==N-1){
        return 0;
    }
    pair<int, int> key = make_pair(pos, use);
    if(memo.count(key))return memo[key];
    double res = 1e100;
    double e = E[use];
    double s = S[use];
    double sum_d = 0;
    for(int i=use; i<pos; i++){
        sum_d += D[i][i+1];
    }

    double d = D[pos][pos+1];
    double elasped = d / s;
    if(pos==use || sum_d + d < e + EPS){
    //cout << pos << " " << sum_d+d << endl;
    //if(sum_d + d < e + EPS){
        res = min<double>(res, rec(pos+1, use) + elasped);
        res = min<double>(res, rec(pos+1, pos+1) + elasped);
    }

    memo[key] = res;
    return res;
}


int main(){
    int T;
    cin >> T;
    REP(tc, T){
        cin >> N >> Q;
        E.resize(N);
        S.resize(N);
        D.assign(N, vector<int>(N));
        REP(i, N){
            cin >> E[i] >> S[i];
        }
        REP(i, N){
            REP(j, N)cin >> D[i][j];
        }
        REP(i, Q){
            int V, U;
            cin >> V >> U;
        }

        memo = map<pair<int, int>, double>();
        double res = rec(0, 0);
        printf("Case #%d: %.9f\n", tc+1, res);
    }
    return 0;
}
