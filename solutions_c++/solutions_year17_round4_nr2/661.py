#include <map>
#include <cmath>
#include <queue>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#define sz(x) (int)((x).size())
#define rep(i,a,b) for (int i=(a); i<(b); i++)
#define per(i,a,b) for (int i=(b-1); i>=(a); i--)
#define debug(x) cout << "$ " << #x << " => " << x << endl
using namespace std;
typedef long long ll;

#define pb push_back
typedef vector<int> vi;
typedef vector<int>::iterator it_vi;

#define fi first
#define se second
#define mp make_pair
typedef pair<int,int> pii;

const int MAX_N = 7 + 1000;
int n,c,m;
///----------------------------------------------
int num[MAX_N];
pii p[MAX_N];
int check(int cnt) {
    int ret=0;
    memset(num,0,sizeof(num)); int tai=1;
    for (int l=0,r; l<m; l=r) {
        for (r=l+1; r<m&&p[r].fi==p[l].fi; r++);
        if (r-l>cnt) ret+=r-l-cnt;
        rep(i,l,r) {
            num[tai]++;
            if (num[tai]>p[l].fi) return -1;
            tai++;
            if (tai>cnt) tai=1;
        }
    }
    return ret;
}
int main() {

    freopen ( "xx.in"  , "r" , stdin  );
    freopen ( "xx.out" , "w" , stdout );

    int tcase=0;
    int icase=0;
    for (scanf("%d",&tcase); ++icase<=tcase; ) {

        ///init

        ///read
        cin>>n>>c>>m;
        memset(num,0,sizeof(num));
        rep(i,0,m) {
            scanf("%d%d",&p[i].fi,&p[i].se);
            num[p[i].se]++;
        }
        int tmp_max=num[1];
        rep(i,2,c+1) tmp_max=max(tmp_max,num[i]);

        ///
        sort(p,p+m);
        pii ret=mp(m,0); {
            for (int l=tmp_max,r=m-1,mid=(l+r)>>1,tmp; l<=r; mid=(l+r)>>1) {
                tmp=check(mid);
                if (~tmp) {
                    r=mid-1;
                    ret=mp(mid,tmp);
                }
                else {
                    l=mid+1;
                }
            }
        }
        printf("Case #%d: %d %d\n",icase,ret.fi,ret.se);

    }

}











