#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <cassert>

using namespace std;
typedef long long LL;

double searchMin(int pos, int N, vector<pair<double,double> >& horses, vector<vector<double> >& total_dist, vector<double>& memo){
    if(pos >= N-1) return 0.0;
    if(memo[pos] >= -0.5) return memo[pos];
    double res = 1.0e+12;
    for(int i = pos+1; i < N; ++i){
        if(total_dist[pos][i] > horses[pos].first) continue;
        double cost = total_dist[pos][i] / horses[pos].second + searchMin(i, N, horses, total_dist, memo);
        res = min(res, cost);
    }
    memo[pos] = res;
    return res;
}

double solve(int N, vector<pair<double,double> >& horses, vector<double>& dist){
    vector<double> memo(N-1, -1.0);
    vector<vector<double> > total_dist(N, vector<double>(N));
    for(int i = 0; i < N; ++i){
        double total = 0.0;
        for(int j = i; j < N; ++j){
            total_dist[i][j] = total;
            if(j < N-1){
                total += dist[j];
            }
        }
    }
    searchMin(0, N, horses, total_dist, memo);
    return memo[0];
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        LL N, Q;
        cin >> N >> Q;
        vector<pair<double,double> > horses(N);
        for(int i = 0; i < N; ++i){
            cin >> horses[i].first >> horses[i].second;
        }
        vector<vector<double> > mat(N, vector<double>(N));
        for(int i = 0; i < N; ++i){
            for(int j = 0; j < N; ++j){
                cin >> mat[i][j];
            }
        }
        vector<double> dist(N-1);
        for(int i = 0; i+1 < N; ++i){
            dist[i] = mat[i][i+1];
        }
        LL U, V;
        for(int q = 0; q < Q; ++q){
            cin >> U >> V;
        }
        //cout << "Case #" << t << ": " << solve(N, horses, dist) << endl;
        printf("Case #%d: %.11f\n", t, solve(N, horses, dist));
    }
    return 0;
}

