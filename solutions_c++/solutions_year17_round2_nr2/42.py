//#include {{{
#include <iostream>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <bitset>
#include <vector>
#include <complex>
#include <algorithm>
using namespace std;
// }}}
// #define {{{
typedef long long ll;
typedef double db;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define de(x) cout << #x << "=" << x << endl
#define rep(i,a,b) for(int i=a;i<(b);++i)
#define per(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
// }}}

char s[] = "ROYGBV";
int cnt[6] , tmp[6] , id[6];

int du[6][6];
string ans;

void dfs(int c){
    rep(i,0,6) if(du[c][i] > 0){
        du[c][i]--;
        du[i][c]--;
        dfs(i);
    }
    ans += s[c];
}

int main(){
    int T;
    scanf("%d",&T);
    rep(i,0,T){
        cerr << i + 1 << endl;
        int n = 0;
        scanf("%d",&n);
        cerr << n << endl;
        rep(i,0,6) scanf("%d",cnt + i);
        rep(i,0,6) cerr << cnt[i] << " ";cerr << endl;
        if(cnt[1] == 0 && cnt[3] == 0 && cnt[5] == 0){
            string ans(n , 0);
            vi v;
            if(n & 1) rep(i,0,n) v.pb(2 * i % n);
            else{
                rep(i,0,n/2) v.pb(i*2);
                rep(i,0,n/2) v.pb(i*2+1);
            }
            rep(i,0,6) id[i] = i;
            sort(id , id + 6 , [&](int a,int b){return cnt[a] > cnt[b];});
            int cur = 0;
            rep(i,0,6) rep(j,0,cnt[id[i]]) ans[v[cur++]] = s[id[i]];
            bool ok = 1;
            rep(i,0,n) ok &= ans[i] != ans[(i+1)%n];
            printf("Case #%d: ",i + 1);
            if(ok) printf("%s\n",ans.c_str());
            else printf("IMPOSSIBLE\n");
        } else {
            memset(du , 0 , sizeof(du));
            rep(i,0,6) tmp[i] = cnt[i];
            rep(i,0,6) cnt[i] *= 2;
            for(int i=0;i<6;i+=2){
                int j=(i+3)%6;
                du[i][j] = du[j][i] = cnt[j];
                cnt[i] -= cnt[j];
                cnt[j] = 0;
            }
            printf("Case #%d: ",i + 1);
            bool ok = 1;
            rep(i,0,6) ok &= cnt[i] >= 0;
            int s = cnt[0] + cnt[2] + cnt[4];
            ok &= s % 2 == 0;
            s /= 2;
            for(int i=0;i<6;i+=2){
                cnt[i] = s - cnt[i];
                ok &= cnt[i] >= 0;
            }
            du[2][4] = du[4][2] = cnt[0];
            du[0][2] = du[2][0] = cnt[4];
            du[0][4] = du[4][0] = cnt[2];
            //rep(i,0,6) rep(j,0,6) printf("%d%c",du[i][j]," \n"[j==5]);
            ans.clear();
            if(ok)
            rep(i,0,6) if(tmp[i]){
                dfs(i);
                break;
            }
            if(sz(ans)) ans.pop_back();
            if(sz(ans) == n) printf("%s\n",ans.c_str());
            else printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
