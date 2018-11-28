#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <queue>
#include <cmath>

using namespace std;
typedef long long LL;

double solve(LL N, LL K, vector<pair<LL,LL> >& cakes){
    priority_queue<double, vector<double>, greater<double> > q;
    sort(cakes.begin(), cakes.end());
    double area = 0.0;
    double best = 0.0;
    for(int i = 0; i < N; ++i){
        double s = cakes[i].first * cakes[i].first * M_PI;
        double c = cakes[i].first * cakes[i].second * 2.0 * M_PI;
        best = max(best, s + c + area);
        if(q.size()+1 >= K && K > 1 && q.top() < c){
            area -= q.top();
            q.pop();
            area += c;
            q.push(c);
        }else if(q.size()+1 >= K){
        }else{
            area += c;
            q.push(c);
        }
    }
    return best;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        LL N, K;
        cin >> N >> K;
        vector<pair<LL,LL> > cakes(N);
        for(int i = 0; i < N; ++i){
            cin >> cakes[i].first >> cakes[i].second;
        }
        double res = solve(N, K, cakes);
        printf("Case #%d: %.11f\n", t, res);
    }
    return 0;
}

