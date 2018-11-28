#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define ri(X) scanf("%d", &(X))
#define rii(X, Y) scanf("%d%d", &(X), &(Y))
#define riii(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define all(a) (a).begin(),(a).end()

const int inf = 0x3f3f3f3f;
const long long infl = 0x3f3f3f3f3f3f3f3fLL;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;

int mod1 = int(1e9) + 7;

#define PI           3.14159265358979323846

vector<pair<ll,ll>> v;

ll dp[1010][1010];
ll dp2[1010][1010];
int main(){

    int tcases;
    ri(tcases);

    for(int cas=1; cas<=tcases; cas++) {
        v.clear();
        memset(dp,0,sizeof(dp));
        memset(dp2,0,sizeof(dp2));

        int n,k;
        rii(n,k);

        for(int i=0; i<n; i++) {
            int r,h;
            rii(r,h);
            v.pb(mp(r,h));
        }
        sort(all(v));

        dp[0][1] = 2*v[0].fs*v[0].sc;
//        dp2[0][1] = v[0].fs;
        for(int i=1; i<n; i++) {
            ll cur = 2*v[i].fs*v[i].sc;
//            ll cur2 = v[i].fs*v[i].fs;
            for(int j=1; j<=k && j<=i+1; j++) {
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1] + cur);
//                if(dp[i-1][j] > dp[i-1][j-1] + cur) {
//                    dp[i][j] = dp[i-1][j];
//                    dp2[i][j] = dp2[i-1][j];
//                } else {
//                    dp[i][j] = dp[i-1][j-1] + cur - dp2[i-1][j-1];
//                    dp2[i][j] = cur2;
//                }
            }
        }
        ll ans = v[0].fs*v[0].fs + 2*v[0].fs*v[0].sc;
        for(int i=1; i<n; i++) 
            ans = max(ans, dp[i-1][k-1] + v[i].fs*v[i].fs + 2*v[i].fs*v[i].sc);

        cout.precision(25);
        cout << "Case #" << cas << ": " << (((double)ans)*PI) << endl;
        //printf("Case #%d: %.f\n", cas);
    }

    return 0;
}
