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
int f1[1500][1000][3];
int f2[1500][1000][3];
int sta[1500];
int main() {

    freopen ( "xx.in" , "r" , stdin );
    freopen ( "xx.out" , "w" , stdout );

    int tcase=0;
    int icase=0;
    for (scanf("%d",&tcase); ++icase<=tcase; ) {

        ///read
        memset(sta,0,sizeof(sta));
        int n1,n2; cin>>n1>>n2;
        rep(i,0,n1) {
            int l,r; scanf("%d%d",&l,&r);
            rep(j,l,r) sta[j]|=1;
        }
        rep(i,0,n2) {
            int l,r; scanf("%d%d",&l,&r);
            rep(j,l,r) sta[j]|=2;
        }


        ///work
        memset(f1,0x3f,sizeof(f1));
        memset(f2,0x3f,sizeof(f2));
        if (!(sta[0]&1)) f1[0][1][1]=0;
        if (!(sta[0]&2)) f2[0][0][2]=0;
        rep(i,1,1440) {
            rep(j,0,721) if (j<=i+1&&i+1-j<=720) {
                rep(k,1,3) {
                    if (sta[i]&k) { continue; }
                    if (k!=1||j>0) {
                        f1[i][j][k]=min(f1[i-1][j-(k==1)][k],f1[i-1][j-(k==1)][3-k]+1);
                        f2[i][j][k]=min(f2[i-1][j-(k==1)][k],f2[i-1][j-(k==1)][3-k]+1);
                    }
                }
            }
        }

        ///print
        int f11 = f1[1439][720][1], f12 = f1[1439][720][2];
        int f21 = f2[1439][720][1], f22 = f2[1439][720][2];
        int ans=min(f11,f22);
        ans=min(ans,f12+1);
        ans=min(ans,f21+1);
        printf("Case #%d: %d\n",icase,ans);

    }

}
















