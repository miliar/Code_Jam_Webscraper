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
#define MAXN 55
using namespace std;

typedef pair<double, double> dd;
double inf = 1000000000000000000.0;
double dp[1010][1010];
double solve(int index, int rem, int k,vector<dd>& nums){
    if(rem == 0){
        return 0;
    }
    if (index == nums.size()) {
        return -inf;
    }
    double& mem = dp[index][rem];
    if (mem != -1.0) {
        return mem;
    }
    if(rem == k){
        return mem = max(M_PI*nums[index].first*nums[index].first +
                   2*M_PI*nums[index].first*nums[index].second + solve(index+1, rem-1, k, nums), solve(index+1, rem, k, nums));
    }
    return mem = max(2*M_PI*nums[index].first*nums[index].second+solve(index+1, rem-1, k,nums), solve(index+1, rem, k, nums));
}

int main(){
    freopen("/Users/Masoud/Desktop/A-large.in", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    int t;
    int ca = 1;
    scanf("%d", &t);
    while(t--){
        for(int i=0; i<1001; i++){
            for (int j=0; j<1001; j++) {
                dp[i][j] = -1.0;
            }
        }
        int n,k;
        scanf("%d %d", &n, &k);
        vector<dd> nums(n);
        for (int i=0; i<n; i++) {
            scanf("%lf %lf", &nums[i].first, &nums[i].second);
        }
        sort(nums.begin(), nums.end());
        reverse(nums.begin(), nums.end());
        printf("Case #%d: %lf\n", ca++, solve(0, k, k, nums));
    }
    return 0;
}

