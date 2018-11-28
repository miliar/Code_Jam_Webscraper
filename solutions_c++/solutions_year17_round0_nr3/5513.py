#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define rep(i,a,n) for (int i=(a);i<(n);i++)
#define per(i,a,n) for (int i=(n)-1;i>=(a);i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) (int)x.size()

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef pair<ll,ll>pll;
typedef vector<pii> vpii;

template<typename T>
T getint() {
    T x=0,p=1;
    char ch;
    do{ch=getchar();}while(ch <= ' ');
    if(ch=='-')p=-1,ch=getchar();
    while(ch>='0'&&ch<='9')x=x*10+ch-'0',ch=getchar();
    return x*p;
}

mt19937 gen(chrono::system_clock::now().time_since_epoch().count());

template<typename T1,typename T2>bool umin(T1 &x,const T2&y){if(x>y)return x=y,true;return false;}
template<typename T1,typename T2>bool umax(T1 &x,const T2&y){if(x<y)return x=y,true;return false;}

const int maxn=(int)1e7+10;
const int inf=(int)1e9+5;
const int mod=(int)1e9+7;
const ll llinf=(ll)1e18+5;
const ld pi=acos(-1.0);

void solve(int n,int k){
    vector<int> have(n+2);
    for(int i = 1; i <= k; ++i) {
        int x=-1,y=-1;
        int best=-1;
        rep(j,1,n+1){
            if(have[j])continue;
            int ls=0,rs=0;
            int z=j-1;
            while(z>=1&&!have[z])z--,ls++;
            z=j+1;
            while(z<=n&&!have[z])z++,rs++;
            if(min(ls,rs)>x){
                x=min(ls,rs);
                y=max(ls,rs);
                best=j;
            }else if(min(ls,rs)==x&&umax(y,max(ls,rs))){
                best=j;
            }
        }
        have[best]=1;
        if(i==k)cout<<y<<' '<<x<<endl;
    }
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    ios_base::sync_with_stdio(0);

    int T;
    cin>>T;
    rep(i,0,T){
        int n,k;
        cin>>n>>k;
        cout<<"Case #"<<i+1<<": ";
        solve(n,k);
    }
    return 0;
}
