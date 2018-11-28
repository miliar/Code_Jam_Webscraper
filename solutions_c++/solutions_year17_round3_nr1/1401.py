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
const ld pi = 3.14159265358979323846264;

ll n,k,ans=0;
ll r[N],h[N];
pll p[N];
ll dp[N][N];

ll rec (ll idx, ll cnt){
    if(cnt==k+1) return 0;

    if(dp[idx][cnt]!=-1) return dp[idx][cnt];

    ll temp=2*p[idx].first*p[idx].second;
    ll ret =0;

    for(int i=0;i<idx;i++){
        ret = max(ret, rec(i,cnt+1));
    }

    return dp[idx][cnt] = ret+temp;
}

int main() {
    fast
    freopen("/Users/gauravsharma/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/gauravsharma/Desktop/CJ/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; kase++) {
        cin>>n>>k;
        ans=0;
        forn(i,n) {
            cin >> r[i] >> h[i];
            p[i].first = r[i];
            p[i].second = h[i];
        }

        sort(p,p+n);

        forn(i,n+1) forn(j,n+1) dp[i][j]=-1;

        forn(i,n){
            ans= max(ans, p[i].first*p[i].first + rec(i,1));
        }

        ld f = ans*pi;

        printf("Case #%d: %.9Lf\n",kase,f);

        //cout << "Case #" << kase << ": " << pi*(ld)ans << endl;
    }
    return 0;
}
