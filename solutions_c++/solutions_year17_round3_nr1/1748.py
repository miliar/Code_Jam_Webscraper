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

double dp[1000][1000];

int main(void){
    freopen("C:/Users/Rideasnail/Downloads/A-large.in","r",stdin);
    freopen("C:/Users/Rideasnail/Downloads/out.txt","w",stdout);

    int tc;
    sci(tc);

    FOR(x,tc)
    {
        int N, K;
        cin >> N;
        cin >> K;


        pair<double,double> pan[N];
        double ans = 0;


        for(int i=0;i<N;i++){
            cin >> pan[i].first;
            cin >> pan[i].second;
        }
        sort(pan, pan+N);

        for(int i=0;i<N;i++){
            for(int ii=0;ii<K;ii++){
                dp[i][ii] = -1;
            }
        }

        for(int i=N-1;i>=0;i--){
            dp[i][K-1] = (pan[i].first * pan[i].first * PI) + (pan[i].first * pan[i].second * 2 * PI);
            if(dp[i][K-1]<dp[i+1][K-1] && i<N-1) {
                dp[i][K-1] = dp[i+1][K-1];
            }
        }

        for(int i=K-2;i>=0;i--){
            for(int ii=N-1;ii>=0;ii--){
                double addHeight = (pan[ii].first * pan[ii].second * 2 * PI);
                if(ii<N-1) {
                    dp[ii][i] = dp[ii+1][i+1] + addHeight;
                }
                if(dp[ii][i]<dp[ii+1][i] && ii<N-1) {
                    dp[ii][i] = dp[ii+1][i];
                }
            }
        }


        printf("Case #%d: %.9lf\n", x+1, dp[0][0]);
    }


    return 0;
}
