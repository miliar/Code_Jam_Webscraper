#include <bits/stdc++.h>
using namespace std;

int t,h1,a1,h2,a2,b,d;
map<pair<pair<pair<int,int>,int>,int>,int> dp;

int solve(int turn, int h, int a, int eh, int ea){
    //cout << turn << " " << h << " " << a << " " << eh << " " << ea << endl;
    pair<pair<pair<int,int>,int>,int> key = {{{h,a},eh},ea};
    if(dp.count(key)) return dp[key];
    dp[key] = 999999999;
    if(eh <= 0) return dp[key] = 0;
    if(h <= 0) return dp[key] = 999999999;
    int res1 = solve(turn+1, h-ea, a, eh-a, ea);
    int res2 = 999999999;
    if(a < eh) res2 = solve(turn+1, h-ea, a+b, eh, ea);
    int res3 = 999999999;
    if(h != h1) res3 = solve(turn+1, h1-ea, a, eh, ea);
    int res4 = 999999999;
    if(ea > 0) res4 = solve(turn+1, h-max(0,ea-d), a, eh, max(0,ea-d));
    int res = min(min(res1,res2),min(res3,res4));
    if(res == 999999999) return dp[key];
    return dp[key] = res+1;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    for(int k = 1; k <= t; k++){
        scanf("%d%d%d%d%d%d",&h1,&a1,&h2,&a2,&b,&d);
        dp.clear();
        int res = solve(0,h1,a1,h2,a2);
        if(res == 999999999) printf("Case #%d: IMPOSSIBLE\n",k);
        else printf("Case #%d: %d\n",k,res);
    }
}