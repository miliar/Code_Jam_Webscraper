#include <bits/stdc++.h>
#include <direct.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define X first
#define Y second


const int alp=26;
const int N=1e2+10;
const int MOD=1e9+7;
const int inf=1e8;
const double eps=1e-8;



int n,m;
int h[4];
int f[N][N][N][4];

void prepare(){
    cin>>n>>m;
    memset(h,0,sizeof(h));
    for(int i=1;i<=n;i++) {
        int val;
        cin>>val;
        h[val%m]++;
    }
    memset(f,-1,sizeof(f));
}

int DP(int m1,int m2,int m3,int over){
    if (m1+m2+m3==0) return 0;
    int& ans=f[m1][m2][m3][over];
    if (ans!=-1) return ans;
    ans=0;
    if (m1) ans=max(ans,DP(m1-1,m2,m3,(over+1)%m));
    if (m2) ans=max(ans,DP(m1,m2-1,m3,(over+2)%m));
    if (m3) ans=max(ans,DP(m1,m2,m3-1,(over+3)%m));
    if (!over) ans++;
    return ans;
}
int solve(){
    return DP(h[1],h[2],h[3],0)+h[0];
}
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;
    cin>>test;
    for(int te=1;te<=test;te++){
        prepare();
        cout<<"Case #"<<te<<": "<<solve()<<'\n';
    }
}
