#include <bits/stdc++.h>
#define rep(i,a,b) for (int i=(a); i<=(b); i++)
using namespace std;
typedef long long ll;
const int MAX_N = 7 + 100;
///----------------------------------------------
int dig[MAX_N];
int main() {

    freopen ( "xx.in"  , "r" , stdin  );
    freopen ( "xx.out" , "w" , stdout );

    int tcase=0;
    int icase=0;
    for (scanf("%d",&tcase); ++icase<=tcase; ) {

        ///init
        printf("Case #%d: ",icase);

        ///read
        ll n; cin>>n;
        int len=!n;
        for (ll tmp=n; tmp; tmp/=10) dig[++len]=tmp%10;
        for (int i=1; i<len+1-i; i++) swap(dig[i],dig[len+1-i]);

        ///prework
        int tmp=1;
        int up_pos=-1;
        for (; tmp<len&&dig[tmp+1]>=dig[tmp]; tmp++) {
            if (dig[tmp+1]>dig[tmp]) up_pos=tmp;
        }

        ///check 1
        if (tmp==len) {
            rep(i,1,len) printf("%d",dig[i]); printf("\n");
            continue;
        }

        ///check 2
        if (~up_pos) {
            dig[up_pos+1]--;
            for (int i=up_pos+2; i<=len; i++) dig[i]=9;
            rep(i,1,len) printf("%d",dig[i]); printf("\n");
            continue;
        }

        ///check 3
        dig[1]--; rep(i,2,len) dig[i]=9;
        int S =  dig[1]==0 ? min(2,len) : 1;
        rep(i,S,len) printf("%d",dig[i]); printf("\n");

    }
}
