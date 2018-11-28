#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <climits>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

using namespace std;
#define fast ios::sync_with_stdio(false);cin.tie(0); cout.tie(0);
#define pb push_back
#define sz(s) (int)s.size()
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define for1(i,n) for(int i=1;i<=(int)n;i++)

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> pll;
typedef vector<ll> vl;
const ll N= (ll)1e3+7;
const ll inf = (ll) 1e16+7;

ll n,m,d,x,y;
ll k[N],s[N];
pll p[N];

int main() {
    fast
    freopen("/Users/gauravsharma/Downloads/A-small-attempt0.in-3.txt", "r", stdin);
    freopen("/Users/gauravsharma/Desktop/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; kase++) {
        cin>>d>>n;
        ll slow = inf;
        for1(i,n){
            cin>>k[i]>>s[i];
            p[i]={k[i],s[i]};
            if(slow>s[i]){
                slow=s[i];
                m=i;
            }
        }

        sort(p+1,p+n+1);
        for1(i,n){
            if(slow>p[i].second){
                slow=p[i].second;
                m=i;
            }
        }

        ld tt,meet,ans=1e18;

        tt = (d - k[m])/(ld)s[m];
        ans= min(ans,(ld)d/tt);

        for(ll i=m-1;i>0;i--){
            tt = (ld)(k[m]-k[i])/(s[i]-s[m]);
            meet = tt*s[m] + k[m];
            if(meet>d){
                tt = (d - k[i])/(ld)s[i];
                ans = min(ans, (ld)d/tt);
            }
        }

        printf("Case #%d: %Lf\n",kase,ans);
        //cout<<"Case #"<<kase<<": "<<ans<<endl;
    }
    return 0;
}
