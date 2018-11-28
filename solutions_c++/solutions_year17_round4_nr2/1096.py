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



int Cnt[1100];
vector<int> g[MAXN];


bool comp(int a,int b){
    return Cnt[a]<Cnt[b];
}

int cnt1[1100];
void solve()
{
    int n,c,m;
    cin >> n >> c >> m;
    int ans=0;
    int cnt = m;
    for(int i=1;i<=n;++i){
        cnt1[i]=0;
    }
    for(int i=1;i<=c;++i){
        g[i].clear();
        Cnt[i]=0;
    }
    for(int i=1;i<=m;++i){
        int pos,x;
        cin >> pos >> x;
        Cnt[x]++;
        g[x].pb(pos);
        cnt1[pos]++;
    }

    int mx = 0;
    vector<int> a;
    for(int i=1;i<=c;++i){
        a.pb(i);
        sort(g[i].begin(),g[i].end());
    }
    bool used[n+1];
    for(ans=0;cnt>0;){
        ans++;
        sort(a.rbegin(),a.rend());
        fill(used,used+n+1,false);
        for(int v:a){

            bool flag  = false;
            int r =1;
            for(int i=0;i<g[v].size();++i){
                int to=g[v][i];
                int e = to;
                while(e>=1){
                    if(used[e]==false){
                        used[e] = true;
                        flag = true;
                        cnt--;
                        r = e+1;
                        break;
                    }
                    e--;
                }
                if(flag){
                    Cnt[v]--;
                    g[v].erase(g[v].begin()+i);
                    break;
                } else {
                    r = to+1;
                }
            }
        }

    }

    int res=0;
    for(int i=1;i<=n;++i){
        res+= max(cnt1[i]-ans,0);
    }

    for(int i=1;i<=c;++i){
        if(Cnt[i]>ans){
            cout << "Bad";
            exit(0);
        }
    }


    cout<<"Case #" <<Test++ <<": "<< ans <<" "<< res<< endl;
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
