#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forab(i,a,b) for( int i = (a); i < (b); i++ )
#define forn(i,n) forab(i,0,n)
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>
#define pcc pair<char,char>

const int MXN = 110;
const double dinf = 1e18;




map<vector<int>, int> dp;
vector< vector< vector< vector< vector<int> > > > > dp1;


int dfs1 (vector<int>& nums) {
    if (dp1[nums[0]][nums[1]][nums[2]][nums[3]][nums[4]] != -1) {
        return dp[nums];
    }
    int mx = 0;
    int p = nums.size() - 1;
    forn(i,p) {
        if (nums[i] > 0) {
            int t = nums[p+1];
            nums[i]--;
            nums[p+1] = (t + i) % p;
            mx = max(mx, (t==0) + dfs(nums));
            nums[i]++;
            nums[p+1] = t;
        }
    }
    return dp1[nums[0]][nums[1]][nums[2]][nums[3]][nums[4]] = mx;
}

int dfs (vector<int>& nums) {
    if (dp.count(nums) > 0) {
        return dp[nums];
    }
    int mx = 0;
    int p = nums.size() - 1;
    forn(i,p) {
        if (nums[i] > 0) {
            int t = nums[p+1];
            nums[i]--;
            nums[p+1] = (t + i) % p;
            mx = max(mx, (t==0) + dfs(nums));
            nums[i]++;
            nums[p+1] = t;
        }
    }
    return dp[nums] = mx;
}

void solve() {
    dp.clear();
    int n,p;
    cin >> n >> p;
    vector<int> nums (p+1);
    forn(i,n) {
        int t;
        scanf("%d", &t);
        nums[t % p]++;
    }

    printf("%d", dfs(nums));
}


int main(){
    freopen("input.txt", "r", stdin);    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    forn(i,T){
        cerr << i << endl;
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }
}
