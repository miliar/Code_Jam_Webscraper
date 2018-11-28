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

int n, p;
int a[110];
int pp[5];

int main(int argc, const char * argv[]) {
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    int T;
    cin >> T;
    REP(ca, 1, T) {
        cin >> n >> p;
        memset(pp, 0, sizeof(pp));
        REP(i, 1, n) {
            cin >> a[i];
            pp[a[i] % p]++;
        }
        
        int ans = 0;
        
        if (p == 3) {
            ans += pp[0];
            int temp = min(pp[1], pp[2]);
            ans += temp;
            pp[1] -= temp; pp[2] -= temp;
            if (pp[1] != 0 || pp[2] != 0) {
                ans += pp[1] / 3;
                ans += pp[2] / 3;
            }
            if (pp[1] % 3 != 0 || pp[2] % 3 != 0) {
                ans++;
            }
        } else if (p == 4){
            ans += pp[0];
            ans += pp[2] / 2;
            int temp = min(pp[1], pp[3]);
            ans += temp;
            pp[1] -= temp; pp[3] -= temp;
            if (pp[1] != 0 || pp[3] != 0) {
                ans += pp[1] / 4;
                ans += pp[3] / 4;
            }
            
            if (pp[1] % 3 != 0 || pp[3] % 3 != 0 || pp[2] % 2 != 0) {
                ans++;
            }
            
        } else {
            ans += pp[0];
            ans += pp[1] / 2;
            if (pp[1] % 2 == 1) {
                ans++;
            }
        }
        
        printf("Case #%d: %d\n", ca, ans);
        
    }
    
    return 0;
}









