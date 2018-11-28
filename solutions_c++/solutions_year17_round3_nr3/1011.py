#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <unordered_map>

using namespace std;

#define Cameron true
#define Jamie false

typedef pair<int, int> P;
typedef pair<P, bool> PP;
int N, K;
const double EPS = 1.e-8;

#define Equal(a, b) abs(a - b) <= EPS

void solve(int tc){
    printf("Case #%d: ", tc);
    cin >> N >> K;
    double U;
    vector<double> P(N, 0.);
    cin >> U;
    for(int i = 0; i < N; i++){
        cin >> P[i];
    }
    sort(P.begin(), P.end());
    
    int minCnt = 1;
    while(!Equal(U, 0)){
        double add;
        if(minCnt < N && (P[minCnt] - P[0]) * minCnt <= U + EPS){
            U -= (P[minCnt] - P[0]) * minCnt;
            add = P[minCnt] - P[0];
        }
        else{
            add = U / minCnt;
            U = 0;
        }
        for(int i = 0; i < minCnt; i++){
            P[i] += add;
        }
        minCnt++;
    }
    
    double res = 1.;
    for(int i = 0; i < N; i++){
        res *= P[i];
    }
    printf("%.8f\n", res);
}

int main(){
    int T;
    cin >> T;
    for(int tc = 1; tc <= T; tc++){
        solve(tc);
    }
    return 0;
}

