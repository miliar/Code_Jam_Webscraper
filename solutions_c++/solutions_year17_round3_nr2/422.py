#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define eps 1e-9
#define MAX 100000
#define MAXL 20
#define MAXE 100000
#define inf 100000000
#define pi acos(-1.0)
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};

bool visJ[1500], visC[1500];
int dp[1450][725][3], start;
int call(int cur, int jam, int person) {
    if(cur == 1440) {
        if(jam == 720 && person != start) return 1;
        else if(jam == 720) return 0;
        return inf;
    }
    if(~dp[cur][jam][person]) return dp[cur][jam][person];
    int ret = inf;
    if(visJ[cur] == false && jam+1 <= 720) {
        int add = 0;
        if(person == 2) add = 1;
        ret = min(ret, call(cur+1, jam+1, 1)+add);
    }
    if(visC[cur] == false && cur+1-jam <= 720) {
        int add = 0;
        if(person == 1) add = 1;
        ret = min(ret, call(cur+1, jam, 2)+add);
    }
    return dp[cur][jam][person] = ret;
}
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    //ios_base::sync_with_stdio(false);

    int ncase, tcase = 1, i, ac, aj, c, d;
    scanf("%d", &ncase);
    while(ncase--) {
        scanf("%d %d", &ac, &aj);
        mem(visC);
        mem(visJ);
        for(i = 0; i < ac; i++) {
            scanf("%d %d", &c, &d);
            for(int j = c; j < d; j++) visC[j] = true;
        }
        for(i = 0; i < aj; i++) {
            scanf("%d %d", &c, &d);
            for(int j = c; j < d; j++) visJ[j] = true;
        }
        int ans = inf;
        if(visJ[0] == false) {
            start = 1;
            _set(dp);
            ans = min(ans, call(1, 1, 1));
        }
        if(visC[0] == false) {
            start = 2;
            _set(dp);
            ans = min(ans, call(1, 0, 2));
        }
        printf("Case #%d: %d\n", tcase++, ans);
    }
    return 0;
}


