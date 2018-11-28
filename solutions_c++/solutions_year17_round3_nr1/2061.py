#include <bits/stdc++.h>
#define rep(i,n) for(auto i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define write(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
#define pb(x) push_back(x);
using namespace std;
typedef long long ll ;
typedef pair<ll,ll> ii;
typedef pair<ll,ii> iii;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<string> vs;
typedef map<ll,ll> mii;
typedef map<string,ll> msi;
typedef set<ll> si;
typedef set<string> ss;
const double pi = 3.1415926535897;
ll t,n,k;
vii pancacke;
double ans=0;

void solve (int pos,double area,int last,int taken){
//printf(" pos %d area %.6f\n",pos,area);
if(taken==k){
    ans=max(ans,area);
    return ;
}
if(pos==n){
    if(taken==k)
    ans=max(ans,area);
    return ;
}
    for(auto i=pos;i<n;i++){
        double surface=(pi*1.0*pancacke[i].first*1.0*pancacke[i].first);
        double hauteur=(2.0*pi*1.0*pancacke[i].first*1.0*pancacke[i].second);
        if(last==-1)
        solve(i+1,hauteur+surface,i,taken+1);
        else
        solve(i+1,area+hauteur,i,taken+1);
    }

    return ;
}




int main()
{
    read("A-small-attempt0.in");
   write("out.out");
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin>>t;
    rep(i,t){
        cin>>n>>k;
        pancacke.clear();
        pancacke.resize(n);
        ans=0.0;

            rep(j,n){
                cin>>pancacke[j].first>>pancacke[j].second;
            }
        sort(pancacke.begin(),pancacke.end());
        reverse(pancacke.begin(),pancacke.end());
        solve(0,0.0,-1,0);

       // cout<<"Case "<<i+1<<": ";
        printf("Case #%lld: %.9f\n",i+1,ans);
    }

    return 0;
}

