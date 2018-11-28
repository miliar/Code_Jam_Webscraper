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
int main()
{
#ifdef LOCAL
    //freopen("in.txt", "r", stdin);
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
#endif
    int t;cin >> t;
    //cout << t << endl;
    double ans;
    int kase = 1;
    while(t--){
        ans = 0;
        double d;
        int n;
        cin >> d >> n;
        for(int i=1;i<=n;i++){
            double p,s;cin >> p >> s;
            ans = max(ans,((d-p)/s));
        }
        printf("Case #%d: %.6lf\n",kase++,d/ans);
    }
    return 0;
}