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
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <time.h>
#include <assert.h>
#define MAXN 10000000
using namespace std;

typedef pair<double, double> dd;
double dist [110][110];
double total_distance[110];
double speed[110];
double dp[110][110];
double solve(int cur_city, int horse, int n){
    
    if(cur_city == n-1)
        return 0;
    
    if(cur_city == 0)
        return dist[0][1]/speed[0] + solve(cur_city+1, 0, n);
    
    double &mem = dp[cur_city][horse];
    if (mem != -1.0) {
        return mem;
    }
    // if you can go to the next city with the same hore, try.
    double total_dist = 0;
    for(int i=horse; i<cur_city; i++){
        total_dist+=dist[i][i+1];
    }
    double ans = 1000000000000000000.0;
    if(total_dist + dist[cur_city][cur_city+1] <= total_distance[horse]){
        ans = min(ans, dist[cur_city][cur_city+1]/speed[horse] + solve(cur_city+1, horse, n));
    }
    if(total_distance[cur_city] >= dist[cur_city][cur_city+1]){
        ans = min(ans, dist[cur_city][cur_city+1]/speed[cur_city] + solve(cur_city+1, cur_city, n));
    }
    return mem = ans;
}
int main(){
    freopen("/Users/Masoud/Desktop/C-small-attempt1.in", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    int t;
    int ca = 1;
    scanf("%d", &t);
    while(t--){
        memset(dist, -1, sizeof(dist));
        memset(total_distance, 0, sizeof(total_distance));
        memset(speed, 0, sizeof(speed));
        for(int i=0; i<110; i++){
            for (int j=0; j<110; j++) {
                dp[i][j] = -1.0;
            }
        }
        int n,q;
        scanf("%d %d", &n, &q);
        for(int i=0; i<n; i++){
            scanf("%lf %lf", &total_distance[i], &speed[i]);
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                scanf("%lf", &dist[i][j]);
            }
        }
        int start,end;
        scanf("%d %d", &start, &end);
        printf("Case #%d: %lf\n", ca++, solve(0, -1, n));
    }
    return 0;
}

