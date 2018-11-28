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


///----------------------------------------------
int num[10];
int main() {

    freopen ( "xx.in"  , "r" , stdin  );
    freopen ( "xx.out"  , "w" , stdout  );

    int tcase=0;
    int icase=0;
    for (scanf("%d",&tcase); ++icase<=tcase; ) {

        printf("Case #%d: ",icase);

        ///init

        ///read
        int n,p; cin>>n>>p;
        memset(num,0,sizeof(num));
        rep(i,0,n) {
            int dig; scanf("%d",&dig);
            num[dig%p]++;
        }

        ///work
        if (p==2) {
            printf("%d\n",num[0]+((num[1]+1)>>1));
        }
        else if (p==3) {
            int ans=num[0];
            int p12=min(num[1],num[2]);
            ans +=p12;
            num[1]-=p12;
            num[2]-=p12;
            if (num[1]) {
                ans+=num[1]/3;
                num[1]%=3;
            }
            else {
                ans+=num[2]/3;
                num[2]%=3;
            }
            if (num[1]||num[2]) ans++;
            printf("%d\n",ans);
        }
        else {
            int ans=num[0];
            int p13=min(num[1],num[3]);
            ans += p13;
            num[1]-=p13;
            num[3]-=p13;
            int p22=(num[2]>>1);
            num[2]=num[2]&1;
            if (num[1]) {
                ans+=num[1]/4;
                num[1]%=4;
            }
            else {
                ans+=num[3]/3;
                num[3]%=3;
            }
            if (num[1]||num[2]||num[3]) ans++;
        }
    }


}











