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

void printAns(ll ans){
    if(ans%2) {
        cout << ans/2 << " " << ans/2;
    } else {
        cout << ans/2 << " " << (ans/2 - 1);
    }
}

int main(void){
    freopen("D:/Code/C-large.in","r",stdin);
    freopen("D:/Code/out.txt","w",stdout);

    int tc;
    sci(tc);

    FOR(i,tc)
    {
        ll n,k,t;
        ll sCount,lCount,sNo;
        ll nsCount, nlCount, nsNo;
        ll ans;
        cin >> n;
        cin >> k;
        t = 0;

        sNo = n;
        sCount = 1;
        lCount = 0;

        while(true) {
            if(k<=t+lCount){
                ans = sNo+1;
                break;
            } else if(k<=t+lCount+sCount){
                ans = sNo;
                break;
            }

            if(sNo%2) {
                nsCount = sCount * 2 + lCount;
                nlCount = lCount;
                nsNo = sNo/2;
            } else {
                nsCount = sCount;
                nlCount = lCount * 2 + sCount;
                nsNo = (sNo/2) - 1;
            }

            sNo = nsNo;
            t += sCount + lCount;
            sCount = nsCount;
            lCount = nlCount;
        }

        cout << "Case #" << i+1 << ": ";
        printAns(ans);
        cout << endl;
    }


    return 0;
}
