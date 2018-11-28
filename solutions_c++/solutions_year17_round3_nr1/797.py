#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;

const int MAX_N = 1e3;
const double PI = acos(-1.0);

int N, K;

inline void maxi(double& a, double b){
    a = max(a, b);
}

struct pan{
    int R, H;
}cake[MAX_N];

bool cmp(const pan& a, const pan& b){
    if (a.R != b. R) return a.R > b.R;
    return a.H > b. H;
}

bool cmp2(LL a, LL b){
    return a > b;
}

vector<LL> vec;
double solve(){
    double ret = 0;
    for (int i = 0; i <= N-K; ++i){       // 底盘
        vec.clear();
        for (int j = i+1; j < N; ++j)
            vec.push_back(2LL * cake[j].R * cake[j].H);
        sort(vec.begin(), vec.end(), cmp2);
        
        LL sum = 2LL * cake[i].R * cake[i].H;
        for (int j = 0; j < K-1; ++j)
            sum += vec[j];
        sum += 1LL * cake[i].R * cake[i].R;
        
        double S = PI * sum;
        maxi(ret, S);
    }
    return ret;
}

int main(){
    freopen("/Users/eajoy/Downloads/A-large.in", "r", stdin);
    freopen("/Users/eajoy/Downloads/A-large.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for (int CASE = 1; CASE <= TEST; ++CASE){
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; ++i){
            scanf("%d%d", &cake[i].R, &cake[i].H);
        }
        sort(cake, cake+N, cmp);
        
        double ans = solve();
        printf("Case #%d: %.10lf\n", CASE, ans);
    }
    return 0;
}
