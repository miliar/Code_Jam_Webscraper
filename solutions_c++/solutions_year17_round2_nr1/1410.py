#include <bits/stdc++.h>
#include <iomanip>
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

int main(void){
    freopen("C:/Users/Rideasnail/Downloads/A-large.in","r",stdin);
    freopen("C:/Users/Rideasnail/Downloads/out.txt","w",stdout);

    int tc;
    sci(tc);

    FOR(x,tc)
    {
        int D, no;

        cin >> D;
        cin >> no;
        int dist;
        int speed;
        double maxTime = 0;
        double curTime;

        for(int i=0;i<no;i++) {
            cin >> dist;
            cin >> speed;
            curTime = (D-dist) * 1.0 / speed;
            if(curTime > maxTime) {
                maxTime = curTime;
            }
        }

        printf("Case #%d: %.7lf\n", x+1, D/maxTime);

        //cout << "Case #" << x+1 << ": " << round((D/maxTime)*10000000)/10000000 << endl;
    }


    return 0;
}
