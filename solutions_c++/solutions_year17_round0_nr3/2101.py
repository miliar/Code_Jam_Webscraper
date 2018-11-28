#include <bits/stdc++.h>
#define rep(i,a,b) for (int i=(a); i<=(b); i++)
#define per(i,a,b) for (int i=(a); i>=(b); i--)
#define debug(x) //cout << #x << " => " << x << endl
using namespace std;
typedef long long ll;
///----------------------------------------------
struct Node { ll num[2],base;
    void init(ll d) { base=d; memset(num,0,sizeof(num)); }
};
int main() {

    freopen ( "xx.in"  , "r" , stdin  );
    freopen ( "xx.out" , "w" , stdout );

    int tcase=0;
    int icase=0;
    for (scanf("%d",&tcase); ++icase<=tcase; ) {

        ///init

        ///read
        ll n; cin>>n; ll k; cin>>k; k--;

        ///prework
        Node now; now.init(n);
        now.num[0]=1;
        Node nex; nex.init((now.base-1)>>1);

        ///work
        for (; k; ) {

            ///cut 1
            ll cut1 = min(now.num[1],k);
            now.num[1]-=cut1; k-=cut1;
            if (now.base&1) nex.num[0]+=cut1, nex.num[1]+=cut1;
                else nex.num[1]+=cut1<<1;
            debug(cut1);

            ///cut 0;
            ll cut0 = min(now.num[0],k);
            now.num[0]-=cut0; k-=cut0;
            if (now.base&1) nex.num[0]+=cut0<<1;
                else nex.num[0]+=cut0, nex.num[1]+=cut0;

            if (!(now.num[0]+now.num[1])) {
                now=nex;
                nex.init((now.base-1)>>1);
            }
            debug(cut0);

            //printf("%d %d %d\n",now.base,now.num[0],now.num[1]);
        }

        ///
        printf("Case #%d: ",icase);
        //debug(now.base);
        if (now.num[1]) printf("%I64d %I64d\n",(now.base+1)>>1,now.base>>1);
            else printf("%I64d %I64d\n",now.base>>1,(now.base-1)>>1);



    }
}
