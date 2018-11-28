#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define X first
#define Y second


const int alp=26;
const int N=60;


int n,m;
int w[N],a[N][N];
int h[N];

void prepare(){
    memset(h,0,sizeof(h));
    cin>>n>>m;
    for(int i=1;i<=n;i++) cin>>w[i];
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++) cin>>a[i][j];
        sort(a[i]+1,a[i]+m+1);
    }
}
ii range(int val,int pos){
    ii ans=ii((val*100+w[pos]*110-1)/(w[pos]*110),(val*100)/(w[pos]*90));
    return ans;
}
int solve(){
    int ans=0;
    fill(h+1,h+n+1,1);
    for(int pack=1;;){
        for(int j=1;j<=n;j++){
            while (h[j]<=m){
                ii nrange=range(a[j][h[j]],j);
                if (nrange.X>nrange.Y) {
                    h[j]++;
                    continue;
                }
                if (nrange.Y<pack) h[j]++;
                else break;
            }
            if (h[j]>m) return ans;
            if (j==1) pack=max(pack,range(a[1][h[1]],1).X);
        }
        int check=0;
        for(int j=1;j<=n;j++){
            ii cr=range(a[j][h[j]],j);
            if (cr.X<=pack&&pack<=cr.Y) check++;
        }
        if (check==n){
            for(int i=1;i<=n;i++) h[i]++;
            ans++;
        }else pack++;
    }
    return ans;
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
