#include <bits/stdc++.h>

using namespace std;
typedef  long long ll;
typedef unsigned long long ull;
int inf_int=2e9;
ll inf_ll=1e17;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define pb push_back
const double pi=3.1415926535898;
#define dout if(debug) cout
#define fi first
#define se second
#define sp setprecision
#define siz(a) a.size()
#define next asdfafgasgasg
#define left asfafgasgasgasgalhs
#define right afszfpfzzk
#define free asfasfasfasafg

const int mod = 1e9 + 7;
const int MAXN = 2e5+100;
bool debug = false;

typedef long double dbl;

int Test = 1;


int cnt[4];
void solve()
{
    int n;
    cin >> n;
    int p;
    cin >> p;
    fill(cnt,cnt+4,0);
    for(int i=1;i<=n;++i){
        int x;
        cin >> x;
        cnt[x%p]++;
    }
    int res=0;
    if(p==2){
        int dp[cnt[0]+3][cnt[1]+3];
        for(int i=0;i<=cnt[0];++i){
            for(int e=0;e<=cnt[1];++e){
                dp[i][e]=0;
            }
        }
        dp[0][0]=0;

        for(int i=0;i<=cnt[0];++i){
            for(int e=0;e<=cnt[1];++e){
                int cur = (e*1)%p;
                dp[i+1][e] = max(dp[i+1][e],dp[i][e] + int(cur==0));
                dp[i][e+1] = max(dp[i][e+1],dp[i][e] + int(cur==0));

            }
        }
        res = dp[cnt[0]][cnt[1]];
    } else if(p==3){
        int dp[cnt[0]+3][cnt[1]+3][cnt[2]+3];
        for(int i=0;i<=cnt[0];++i){
            for(int e=0;e<=cnt[1];++e){
                for(int j=0;j<=cnt[2];++j)
                    dp[i][e][j]=0;
            }
        }

        for(int i=0;i<=cnt[0];++i){
            for(int e=0;e<=cnt[1];++e)
                for(int j=0;j<=cnt[2];++j){
                    int cur = (e*1 + j*2)%p;
                    dp[i+1][e][j] = max(dp[i+1][e][j], dp[i][e][j] + int(cur==0));
                    dp[i][e+1][j] = max(dp[i][e+1][j], dp[i][e][j] + int(cur==0));
                    dp[i][e][j+1] = max(dp[i][e][j+1], dp[i][e][j] + int(cur==0));
            }
        }
        res = dp[cnt[0]][cnt[1]][cnt[2]];
    } else {
        int dp[cnt[0]+3][cnt[1]+3][cnt[2]+3][cnt[3]+3];
        for(int i=0;i<=cnt[0];++i){
            for(int e=0;e<=cnt[1];++e){
                for(int j=0;j<=cnt[2];++j)
                    for(int f=0;f<=cnt[3];++f)
                        dp[i][e][j][f]=0;
            }
        }

        for(int i=0;i<=cnt[0];++i){
            for(int e=0;e<=cnt[1];++e)
                for(int j=0;j<=cnt[2];++j)
                    for(int f=0;f<=cnt[3];++f){
                        int cur = (e*1 + j*2 + f*3)%p;
                        dp[i+1][e][j][f] = max(dp[i+1][e][j][f], dp[i][e][j][f] + int(cur==0));
                        dp[i][e+1][j][f] = max(dp[i][e+1][j][f], dp[i][e][j][f] + int(cur==0));
                        dp[i][e][j+1][f] = max(dp[i][e][j+1][f], dp[i][e][j][f] + int(cur==0));
                        dp[i][e][j][f+1] = max(dp[i][e][j][f+1], dp[i][e][j][f] + int(cur==0));
            }
        }
        res = dp[cnt[0]][cnt[1]][cnt[2]][cnt[3]];


    }

    cout << "Case #"<<Test++<<": "<<res<<"\n";
}


#define FILE "close-vertices"
int main()
{
        #ifdef zxc
            freopen("input.txt","r",stdin);
          freopen("output.txt","w",stdout);
        #else
        #endif // zxc


         ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);


        int t=1;
        cin >> t;
        while(t--)
           solve();
        return 0;
}
