#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <functional>
#include <map>
#include <bitset>

#define INF 0x7fffffff
#define REP(i,j,k) for(int i = j;i <= k;i++)
#define squr(x) (x) * (x)
#define lowbit(x) (x&(-x))
#define getint(x) scanf("%d", &(x))

typedef long long LL;

using namespace std;

const int MAXN = 1010;

int n, m, c;
int p, b;
int cot[MAXN];
int num[MAXN];

int main(int argc, const char * argv[]) {
    //freopen("B-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int T;
    cin >> T;
    REP(ca, 1, T) {
        cin >> n >> c >> m;
        memset(cot, 0, sizeof(cot));
        memset(num, 0, sizeof(num));
        int ans1 = 0, ans2 = 0;
        REP(i, 1, m) {
            cin >> p >> b;
            cot[p]++;
            num[b]++;
        }
        
        int sum = 0;
        REP(i, 1, n) {
            sum += cot[i];
            ans1 = max(ans1, (sum - 1) / i + 1);
        }
        
        REP(i, 1, c) {
            ans1 = max(ans1, num[i]);
        }
        
        REP(i, 1, n) {
            ans2 += max(0, cot[i] - ans1);
        }
        
        printf("Case #%d: %d %d\n", ca, ans1, ans2);
        
    }
    
    return 0;
}









