#include<bits/stdc++.h>
//#define int long long
#define ll long long
#define mkp make_pair
#define pb push_back
#define pii pair<int,int>
#define sqr(x) (x) * (x)
#define all(a) (a).begin(),(a).end()
#define inf (int)1e9
using namespace std;

const int N = 1e2 +121;

char ch[N][N];
int i,j,x,y,n,m,t;
int xmin[N][N],xmax[N][N],ymax[N][N],ymin[N][N];

bool check(int x1,int y1,int x2,int y2,char ch_){
    for(int i=x1;i<=x2;++i)
        for(int j=y1;j<=y2;++j)
        if(ch[i][j]!='?' && ch[i][j]!=ch_)return 0;
    return 1;
}

void up(int x1,int y1,int x2,int y2,char ch_){
    for(int i=x1;i<=x2;++i)
        for(int j=y1;j<=y2;++j)
        ch[i][j] = ch_;
}

void f(int i,int j)
{
    for(int x1=1;x1<=n;++x1)
        for(int y1=1;y1<=m;++y1)
    if(check(x1,y1,i,j,ch[i][j])){
       for(int y2=m;y2>=y1;--y2)
        for(int x2=n;x2>=x1;--x2)
            if(i>=x1&&i<=x2&&j>=y1&&j<=y2&&check(x1,y1,x2,y2,ch[i][j])){
            up(x1,y1,x2,y2,ch[i][j]);
            return;
            }
    }
}
int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("A-large (1).in","r",stdin);freopen("output.txt","w",stdout);

    cin>>t;
    for(int test=1;test<=t;++test){
           cout<<"Case #"<<test<<":\n";
        cin >> n >> m;

        for(int i=1;i<=n;++i)
        for(int j=1;j<=m;++j){
            cin>>ch[i][j];
        }

        for(int i=1;i<=n;++i)
        for(int j=1;j<=m;++j){
            if(ch[i][j]!='?')
                f(i,j);
        }
        for(int i=1;i<=n;++i){
        for(int j=1;j<=m;++j){
            if(ch[i][j]=='?')cout<<"oops\n";
            cout<<ch[i][j];
        }
        cout<<endl;
        }

    }
}
