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

#define mp make_pair
int z=1;


void solve()
{

    int n;
    cin >> n;
    int R, O, Y, G, B, V;
    cin >> R >> O >> Y >> G >> B >> V;
    string ans="";

    priority_queue<pair<pii,char> > q;

    pair<pii,int> r=mp(mp(R,0),'R'),y={{Y,0},'Y'},b={{B,0},'B'};
    if(R >= max(Y,B)) {
        r.fi.se=1;
    } else if(Y>=B){
        y.fi.se=1;
    } else {
        b.fi.se=1;
    }

    q.push(r);
    q.push(y);
    q.push(b);
    char last='#';
    for(int i=1;i<=n;++i){
        vector<pair<pii,int> > a;
        while(!q.empty()) {
            auto x = q.top(); q.pop();
            a.pb(x);
        }

        int e=0;
        for(auto x:a){
            if(x.fi.fi>0 && x.se!=last){
                ans.pb(x.se);

                a[e].fi.fi--;
                last=x.se;
                break;
            }
            e++;
        }
        for(auto x:a){
            q.push(x);
        }
    }
    if(ans.size()!=n || ans.back()==ans[0]){
        ans="IMPOSSIBLE";
    }

    cout<<fixed << setprecision(15)<<"Case #"<<z++<<": "<<ans<<endl;


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
