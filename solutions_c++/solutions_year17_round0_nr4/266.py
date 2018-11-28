#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define X first
#define Y second

const int N=1e2+10;


int n;
int bis[2][N<<1],rook[2][N];
int b[N][N],ansb[N][N],ansr[N][N];
vector <ii> ansc;

void markbis(int x,int y){
    bis[0][x+y]=1;
    bis[1][y-x+N]=1;
    ansb[x][y]++;
}
void markrook(int x,int y){
    rook[0][x]=1;
    rook[1][y]=1;
    ansr[x][y]++;
}
void prepare(){
    memset(bis,0,sizeof(bis));
    memset(rook,0,sizeof(rook));
    memset(ansb,0,sizeof(ansb));
    memset(ansr,0,sizeof(ansr));
    memset(b,0,sizeof(b));
    ansc.clear();
    int m;
    cin>>n>>m;
    while (m--){
        int x,y;
        char ch;
        cin>>ch>>x>>y;
        x--;y--;
        if (ch=='o'){
            markbis(x,y);
            markrook(x,y);
            b[x][y]=2;
        }
        if (ch=='x'){
            markrook(x,y);
            b[x][y]=1;
        }
        if (ch=='+'){
            markbis(x,y);
            b[x][y]=1;
        }
    }
}
void solve(){
    ///rook
    for(int i=0;i<n;i++) if (!rook[0][i])
        for(int j=0;j<n;j++) if (!rook[1][j]){
            markrook(i,j);
            break;
        }
    ///bishop
    for(int i=0;i<n;i++) {
        if (!bis[0][i])
            for(int x=i,y=0;x>=0;x--,y++) if (x<n&&y<n&&!bis[1][y-x+N]){
                markbis(x,y);
                break;
            }
        if (!bis[0][2*n-2-i])
            for(int x=2*n-2-i,y=0;x>=0;x--,y++) if (x<n&&y<n&&!bis[1][y-x+N]){
                markbis(x,y);
                break;
            }
    }
    int anss=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++) {
            int val=ansb[i][j]+ansr[i][j];
            anss+=val;
            if (val!=b[i][j]) ansc.push_back(ii(i,j));
        }
    cout<<anss<<" "<<ansc.size()<<'\n';
    for(auto i:ansc){
        if (ansb[i.X][i.Y]&&ansr[i.X][i.Y]) cout<<"o";
        else if (ansb[i.X][i.Y]) cout<<"+";
        else cout<<"x";
        cout<<" "<<i.X+1<<" "<<i.Y+1<<'\n';
    }
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
