#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define X first
#define Y second


const int alp=26;
const int N=50;

string s[N];
int h[alp][N][N];

int n,m;
int get(int xa,int ya,int xb,int yb,int cur){
    return h[cur][xb][yb]-h[cur][xa-1][yb]-h[cur][xb][ya-1]+h[cur][xa-1][ya-1];
}
void prepare(){
    cin>>n>>m;
    for(int i=1;i<=n;i++) {
        cin>>s[i];
        s[i]='@'+s[i];
        for(int j=1;j<=m;j++)
            for(int ni=0;ni<alp;ni++) h[ni][i][j]=h[ni][i-1][j]+h[ni][i][j-1]-h[ni][i-1][j-1]+(s[i][j]=='A'+ni);
    }
}

void split(int xa,int ya,int xb,int yb){
    ///try to split horizontal
    for(int i=xb-1;i>xa;i--){
        int diff=0,nL=0,nR=0;
        for(int j=0;j<alp;j++) {
            int cL=get(xa,ya,i-1,yb-1,j);
            int cR=get(i,ya,xb-1,yb-1,j);
            if (cL) nL++;
            if (cR) nR++;
            if (cL&&cR) diff++;
        }
        if (diff==0){
            if (nL==0){
                split(i,ya,xb,yb);
                for(int ni=i-1;ni>=xa;ni--)
                    for(int j=ya;j<yb;j++) s[ni][j]=s[ni+1][j];
                return;
            }
            if (nR==0){
                split(xa,ya,i,yb);
                for(int ni=i;ni<xb;ni++)
                    for(int j=ya;j<yb;j++) s[ni][j]=s[ni-1][j];
                return;
            }
            split(xa,ya,i,yb);
            split(i,ya,xb,yb);
            return;
        }
    }
    for(int j=yb-1;j>ya;j--){
        int diff=0,nL=0,nR=0;
        for(int i=0;i<alp;i++) {
            int cL=get(xa,ya,xb-1,j-1,i);
            int cR=get(xa,j,xb-1,yb-1,i);
            if (cL) nL++;
            if (cR) nR++;
            if (cL&&cR) diff++;
        }
        if (diff==0){
            if (nL==0){
                split(xa,j,xb,yb);
                for(int nj=j-1;nj>=ya;nj--)
                    for(int i=xa;i<xb;i++) s[i][nj]=s[i][nj+1];
                return;
            }
            if (nR==0){
                split(xa,ya,xb,j);
                for(int nj=j;nj<yb;nj++)
                    for(int i=xa;i<xb;i++) s[i][nj]=s[i][nj-1];
                return;
            }
            split(xa,j,xb,yb);
            split(xa,ya,xb,j);
            return;
        }
    }
}
void solve(){
    split(1,1,n+1,m+1);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++) cout<<s[i][j];
        cout<<'\n';
    }
}
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;
    cin>>test;
    for(int te=1;te<=test;te++){
        prepare();
        cout<<"Case #"<<te<<":\n";
        solve();
    }
}
