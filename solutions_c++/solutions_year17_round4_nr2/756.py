#include <bits/stdc++.h>
#include <direct.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define X first
#define Y second


const int alp=26;
const int N=1e3+10;
const int MOD=1e9+7;
const int inf=1e8;
const double eps=1e-8;



int n,m,k;
int h[N][2];
int f[4],tf[4];

void prepare(){
    cin>>n>>k>>m;
    memset(h,0,sizeof(h));
    for(int i=1;i<=m;i++){
        int x,val;
        cin>>x>>val;
        h[x][val-1]++;
    }
}
int check(int ride){
    int ans=0;
    memset(f,0,sizeof(f));
    f[0]=ride-h[1][0]-h[1][1];
    f[1]=h[1][0];
    f[2]=h[1][1];
    for(int pos=2;pos<=n;pos++){
        int rem=ride;
        for(int i=0;i<=1;i++)
            for(int tmp=1;tmp<=h[pos][i];tmp++)
                for(int j=0;j<5;j++) {
                    if (j==4) return m+1;
                    if ((!(j&(1<<i)))&&f[j]){
                        f[j]--;f[j|(1<<i)]++;
                        if (rem) rem--;
                        else ans++;
                        break;
                    }
                }
//        for(int j=0;j<4;j++) f[j]+=tf[j];
//        memset(tf,0,sizeof(tf));
    }
//    cout<<ride<<"->"<<ans<<'\n';
    return ans;
}
void solve(){
    int L=h[1][0]+h[1][1],R=m;
    while (L<=R){
        int mid=(L+R)/2;
        if (check(mid)!=m+1) R=mid-1;
        else L=mid+1;
    }
    cout<<L<<" "<<check(L)<<'\n';
}
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;
    cin>>test;
    for(int te=1;te<=test;te++){
        prepare();
        cout<<"Case #"<<te<<": ";
        solve();
    }
}
