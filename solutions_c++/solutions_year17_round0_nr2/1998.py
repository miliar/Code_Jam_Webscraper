#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sci(x) scanf("%d",&x)
#define scs(x) scanf("%s",&x)

ll recalculate(ll ans) {
    ll mult = 1;
    ll nans = ans;
    while((nans/mult)%10 < (nans/(mult*10))%10) {
        nans -= ((nans/mult)%10) * mult;
        nans += (mult*9);
        nans -= (mult*10);
        mult *= 10;
    }

    return nans;
}

int main(void){
    freopen("D:/Code/B-large.in","r",stdin);
    freopen("D:/Code/out.txt","w",stdout);

    int tc;
    sci(tc);

    FOR(i,tc)
    {
        ll inp,cur;
        ll ans = 0;
        ll div = 1;
        ll prev = 0;
        bool gg = false;
        cin >> inp;
        while(inp > div) {
            div*=10;
        }
        while(div>0){
            cur = (inp/div)%10;
            if(gg) {
                ans = (ans*10) + 9;
            } else {
                if(cur>=prev){
                    ans = (ans*10) + cur;
                    prev = cur;
                } else {
                    gg = true;
                    ans = recalculate(ans-1);
                    ans = (ans*10) + 9;
                }
            }
            div/=10;
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }


    return 0;
}
