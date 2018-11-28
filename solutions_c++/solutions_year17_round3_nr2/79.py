#pragma GCC optimize("O3")
#include <bits/stdc++.h>

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define files(name) name!=""?freopen(name".in","r",stdin),freopen(name".out","w",stdout):0
#define files_ds(name) name!=""?freopen(name".dat","r",stdin),freopen(name".sol","w",stdout):0
#define all(a) a.begin(),a.end()
#define len(a) (int)(a.size())
#define elif else if
#define mp make_pair
#define pb push_back
#define fir first
#define sec second

using namespace std;
#define int long long

typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long double ld;
typedef long long ll;

const int arr=2e5+10;
const int ar=2e3+10;
const ld pi=acos(-1);
const ld eps=1e-10;
const ll md=1e9+7;

///---program start---///

#define arr (int)(24*60-1)

int test_num;
bool is_close[2][arr+10];
int dp[arr+10][arr+10][2][2];

void minimize(int& a,int b)
{
    if (a>b) a=b;
}

void solve()
{
    int n,m;
    cin>>n>>m;
    memset(is_close,0,sizeof(is_close));
    while (n--){
        int l,r;
        cin>>l>>r;
        while (l<r){
            is_close[0][l++]=1;
        }
    }
    while (m--){
        int l,r;
        cin>>l>>r;
        while (l<r){
            is_close[1][l++]=1;
        }
    }
    for (int i1=0;i1<arr+10;i1++){
        for (int i2=0;i2<arr+10;i2++){
            for (int i3=0;i3<2;i3++){
                for (int i4=0;i4<2;i4++){
                    dp[i1][i2][i3][i4]=1e9;
                }
            }
        }
    }
    if (!is_close[0][0]){
        dp[0][0][0][0]=0;
    }
    if (!is_close[1][0]){
        dp[0][1][1][1]=0;
    }
    for (int i=0;i<arr;i++){
        for (int j=0;j<=i+1;j++){
            for (int k=0;k<2;k++){
                for (int l=0;l<2;l++){
                    if (!is_close[l][i+1]){
                        minimize(dp[i+1][j+(l==1)][k][l],dp[i][j][k][l]);
                    }
                    if (!is_close[l^1][i+1]){
                        minimize(dp[i+1][j+(l==0)][k][l^1],dp[i][j][k][l]+1);
                    }
                }
            }
        }
    }
    int ans=1e9;
    for (int i=0;i<2;i++){
        for (int j=0;j<2;j++){
            minimize(ans,dp[arr][720][i][j]+(i!=j));
        }
    }

    cout<<"Case #"<<test_num<<": "<<ans<<"\n";
}

main()
{
    #ifdef I_love_Maria_Ivanova
        files("barik");
        freopen("debug.txt","w",stderr);
    #else
        files("");
        files_ds("");
    #endif

    fast;
    int test;
    cin>>test;
    while (test--){
        test_num++;
        solve();
    }
}
