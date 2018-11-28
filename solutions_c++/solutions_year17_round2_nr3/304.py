#include <bits/stdc++.h>

using namespace std;
typedef  long long ll;
typedef unsigned long long ull;
int inf_int=1e9;
ll inf_ll=1e16;
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

const int mod = 1e9 + 9;
const int MAXN = 2e5+100;
bool debug = false;

typedef long double dbl;


int z=1;

ll E[MAXN];

dbl S[MAXN];

ll D[150][150];




dbl dis[150];
char used[MAXN];
int n;
dbl dey(int s,int f){
    fill(used,used+n+1,false);
    fill(dis,dis+n+1,inf_ll);
    dis[s]=0;
    for(int j=1;j<=n;++j){
        int ind=-1;
        for(int i=1;i<=n;++i){
            if(!used[i] && (ind==-1 || dis[i]<dis[ind]))
                ind=i;
        }

        for(int i=1;i<=n;++i){
            if(D[ind][i]<=E[ind]){
                dis[i]=min(dis[i],dis[ind] + D[ind][i]/S[ind]);
            }
        }
        used[ind]=1;
    }
    return dis[f];
}
void solve()
{
    int q;
    cin >> n >> q;
    for(int i=1;i<=n;++i){
        cin >> E[i] >> S[i];
    }
    for(int i=1;i<=n;++i){
        for(int e=1;e<=n;++e){
            cin >> D[i][e];
            if(D[i][e]==-1){
                D[i][e]=inf_ll;
            }
        }
        D[i][i]=0;
    }

    for(int k=1;k<=n;++k){
        for(int i=1;i<=n;++i){
            for(int e=1;e<=n;e++){
                D[i][e]=min(D[i][e],D[i][k]+D[k][e]);
            }
        }
    }
    cout<<fixed << setprecision(15)<<"Case #"<<z++<<":";
    for(int j=1;j<=q;++j){
        int v,s;
        cin >> v >> s;

        cout <<" "<<dey(v,s);
    }


     cout <<"\n";

}


#define FILE "shifts"
int main()
{
        #ifdef zxc
            freopen("input.txt","r",stdin);
           freopen("output.txt","w",stdout);
        #else
        #endif // zxc


       if(!debug)
       {
            ios_base::sync_with_stdio(0);
            cin.tie(0);
            cout.tie(0);
       }

        int t=1;
        cin >> t;
        while(t--)
           solve();
        return 0;
}
