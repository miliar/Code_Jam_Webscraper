#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define CL(A,I) (memset(A,I,sizeof(A)))

#define FOR(i, m, n) for (int i=m; i < n; i++)
#define F(n) FOR(i,0,n)
#define FF(n) FOR(j,0,n)

#define D(X) cout<<"  "<<#X": "<<X<<endl;

using ll=long long;
using ii=pair<ll,ll>;
using vi=vector<ll>;
using vii=vector<ii>;

#define aa first
#define bb second

#define EPS (1e-9)
#define EQ(A,B) (A+EPS>B&&A-EPS<B)

int r,c;
string grid[27];

void process(){
    cin>>r>>c;
    F(r)cin>>grid[i];


    F(r){
        char x='?';
        FF(c)if(grid[i][j]!='?'){x=grid[i][j];break;}
        FF(c)if(grid[i][j]=='?')grid[i][j]=x;
            else x=grid[i][j];
    }

    F(r)FF(c)if(i>0&&grid[i][j]=='?')grid[i][j]=grid[i-1][j];
    F(r)FF(c)if(i<r-1&&grid[i][j]=='?')grid[i][j]=grid[i+1][j];
    for(int i=r-1;i>=0;i--)FF(c)if(i>0&&grid[i][j]=='?')grid[i][j]=grid[i-1][j];
    for(int i=r-1;i>=0;i--)FF(c)if(i<r-1&&grid[i][j]=='?')grid[i][j]=grid[i+1][j];

    F(r)
    cout<<grid[i]<<endl;
}

int main() {
    int t;cin>>t;
    F(t){
        cout<<"Case #"<<i+1<<": "<<endl;
        process();
        // cout<<endl;
    }
    return 0;
}