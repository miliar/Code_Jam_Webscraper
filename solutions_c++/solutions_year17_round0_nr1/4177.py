#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
//#pragma comment(linker, "/STACK:1024000000,1024000000")

using namespace std;

#define ll long long
#define SZ(x) ((int)(x).size()) 
#define ALL(v) (v).begin(), (v).end()
#define foreach(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++ i)
#define reveach(i, v) for (__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); ++ i) 
#define REP(i,a,n) for ( int i=a; i<int(n); i++ )
#define FOR(i,a,n) for ( int i=n-1; i>= int(a);i-- )
#define lson rt<<1, L, m
#define rson rt<<1|1, m, R
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define fi first
#define se second
#define CLR(a, b) memset(a, b, sizeof(a))
#define Max(a, b) a = max(a, b)
#define Min(a, b) a = min(a, b)
#define lowbit(x) (x) & (-(x))
const int N = 1e3 + 7;

int n;
char s[N];
int k;
bool solve(){
    REP(i, 0, n){
        if(s[i] == '-')
            return false;
    }
    return true;
}
int main(){
#ifdef LOCAL_TEST
	freopen("in.txt","r",stdin);
#endif
	freopen("out.txt","w",stdout);
    int T, kase = 0;
    scanf("%d", &T);
    while(T --){
        scanf("%s", s);
        scanf("%d", &k);
        n = strlen(s);
        int res = 0;
        REP(i, 0, n - k + 1){
            if(s[i] == '-'){
                REP(j, i, i + k){
                    s[j] = s[j] == '-' ? '+' : '-';
                }
                res ++;
            }
        }
        printf("Case #%d: ", ++ kase);
        if(solve()){
            printf("%d\n", res);
        }
        else{
            puts("IMPOSSIBLE");
        }
    }
    return 0;
}
