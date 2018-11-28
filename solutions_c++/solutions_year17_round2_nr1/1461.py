#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

//int dir[] = { 0, -1, 0, 1, 0 };
const int MAX_NUM = 1000;
int T = 0, D, N;
int dist[MAX_NUM], speed[MAX_NUM];

double calc() {
    double maxTime = 0.0;
    for (int i = 0; i < N; i++) {
        double d = D - dist[i];
        maxTime = max(maxTime, d / speed[i]);
    }
    
    return D / maxTime;
}
int main() {
    freopen("1a.in", "r", stdin);
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &D, &N);
        for (int h = 0; h < N; h++) {
            scanf("%d %d\n", &dist[h], &speed[h]);
        }
        
        printf("Case #%d: %.6f\n", t, calc());
    }
    return 0;
}
