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
///----------------------------------------------
double dig[MAX_N];
double can[MAX_N];
int main() {
	freopen("C.out", "w", stdout);
    int tcase=0;
    int icase=0;
    for (scanf("%d",&tcase); ++icase<=tcase; ) {

        ///init

        ///read
        int n,m; cin>>n>>m;
        double U; cin>>U;
        rep(i,0,n) cin>>dig[i];

        ///prework
        sort(dig,dig+n); dig[n]=1.0;
        rep(i,0,n) {
            double ned=dig[i+1]-dig[i];
            can[i]=min(ned,U/(i+1));
            U-=can[i]*(i+1);
        }
        double sum=0.0;
        double ans=1.0;
        per(i,0,n) {
            sum+=can[i];
            //debug(sum+dig[i]);
            ans=ans*(dig[i]+sum);
            //debug(ans);
        }

        printf("Case #%d: %.8f\n",icase,ans);

    }

}

