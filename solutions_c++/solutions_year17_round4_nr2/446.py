/*  ^^ ====== ^^ 
ID: meixiuxiu
PROG: test
LANG: C++11
*/
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
#include <bitset>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int ,int> pii;
#define MEM(a,b) memset(a,b,sizeof a)
#define CLR(a) memset(a,0,sizeof a);
#define pi acos(-1.0)
#define maxn 40000
#define maxv 100005
const int inf = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
int dp[1001];
int sum[1001];
int ans[1001];
int main()
{
#ifdef LOCAL
	freopen("B-large (1).in", "r", stdin);
	freopen("out.txt","w",stdout);
#endif
    int kase = 1;
    int t;cin >> t;
    int n,c,m;
    while(t--){
        //mp.clear();
        cin >> n >> c >> m;
        MEM(sum,0);
        MEM(dp,0);
        MEM(ans,0);
        int l=0,r = m;
        for(int i=1;i<=m;i++){
            int p,b;cin >> p >> b;
            dp[p]++;
            ans[b]++;
        }
        for(int i=1;i<=n;i++){
            sum[i] = dp[i]+sum[i-1];
        }
        for(int i=1;i<=c;i++){
            l = max(ans[i],l);
        }
        while(l < r){
            int mid = (l+r)>>1;
            int check = 1;
            for(int i=1;i<=n;i++){
                if(mid*i<sum[i])check = 0;
            }
            if(check){
                r = mid;
            }
            else l = mid+1;
        }
        int tot = 0;
        for(int i=1;i<=n;i++){
            tot += max(0,dp[i]-l);
        }
        printf("Case #%d: %d %d\n",kase++,l,tot);
    }
	return 0;
}








