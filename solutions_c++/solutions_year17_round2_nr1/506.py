#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define PB push_back
#define MP make_pair
#define clr(a,b)    (memset(a,b,sizeof(a)))
#define rep(i,a)    for(int i=0; i<(int)a.size(); i++)

const int INF = 0x3f3f3f3f;
const double eps = 1E-8;

class Solution {

public:
    int dp[22][22];
    int val[22];
    int sum[22];

    int dfs(int l, int r)
    {
        if(dp[l][r] != -1) return dp[l][r];
        if(l > r) return 0;
        if(l == r) return val[l];

        int v1 = sum[r] - sum[l] - dfs(l+1, r) + val[l];
        int v2 = sum[r-1] - sum[l-1] - dfs(l, r-1) + val[r];
        int ret;

        ret = max(v1, v2);

        return dp[l][r] = ret;
    }

    bool PredictTheWinner(vector<int>& nums) {
        int sz = nums.size();
        sum[0] = 0;
        for(int i=0; i<sz; i++)
        {
            val[i+1] = nums[i];
            sum[i+1] = sum[i] + nums[i];
        }
        memset(dp, -1, sizeof(dp));

        int v = dfs(1, sz);
        int v2 = sum[sz] - v;

        return v >= v2;
    }
};

int main()
{
    Solution obj = Solution();
    vector<int> a = {1, 5, 233, 7};
    int v = obj.PredictTheWinner(a);
    cout << v << endl;


}
