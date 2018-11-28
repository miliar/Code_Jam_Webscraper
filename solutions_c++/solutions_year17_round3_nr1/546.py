#include <bits/stdc++.h>
#define rep(i,a,b) for (int i=(a); i<(b); i++)
#define per(i,a,b) for (int i=(b-1); i>=(a); i--)
#define debug(x) cout << #x << " => " << x << endl
using namespace std;
typedef long long ll;

#define fi first
#define se second
#define mp make_pair
typedef pair<int,int> pii;

#define pb push_back
typedef vector<int> vi;
typedef vi::iterator it_vi;

const int MAX_N = 7 + 1000;
const double Pi = acos(-1.0);
///----------------------------------------------
pii p[MAX_N];
pii tmp[MAX_N];
bool cmp(const pii&A,const pii&B) {
    return (ll)A.fi*A.se>(ll)B.fi*B.se;
}

int main() {

    freopen ( "xx.in" , "r" , stdin );
    freopen ( "xx.out" , "w" , stdout );

    int tcase=0;
    int icase=0;
    for (scanf("%d",&tcase); ++icase<=tcase; ) {

        ///read
        int n,k; scanf("%d%d",&n,&k);
        rep(i,0,n) scanf("%d%d",&p[i].fi,&p[i].se);

        ///work
        double ans=0.0;
        rep(i,0,n) {
            int tn=0;
            rep(j,0,n)
                if (j!=i&&p[j].fi<=p[i].fi)
                    tmp[tn++]=mp(p[j].se,p[j].fi);
            sort(tmp,tmp+tn,cmp);

            double ret = Pi*p[i].fi*p[i].fi + 2.0*Pi*p[i].fi*p[i].se;
            if (tn<k-1) continue;
            rep(j,0,k-1) {
                pii u=tmp[j];
                ret+=2.0*Pi*u.se*u.fi;
            }
            ans=max(ans,ret);
        }

        ///print
        printf("Case #%d: %.16f\n",icase,ans);


    }



}









