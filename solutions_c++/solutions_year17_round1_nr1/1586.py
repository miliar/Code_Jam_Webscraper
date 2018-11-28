#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define mod(a,b) ((a)%(b)+(b))%(b)
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define rep(i,n) for(int (i)=0;(i)<int((n));(i)++)
#define r first
#define c second

void solve(){
    int R,C;
    char CK[30][30];
    scanf("%d %d",&R,&C);
    char Cr;
    rep(i,R)
        scanf("%s",CK[i]);
    rep(i,R){
        Cr='?';
        rep(j,C){
            if(CK[i][j]=='?'){
                if(Cr!='?')
                    CK[i][j]=Cr;
            }
            else
                Cr=CK[i][j];
        }
    }
    rep(i,R){
        Cr='?';
        rep(j,C){
            if(CK[i][C-j-1]=='?'){
                if(Cr!='?')
                    CK[i][C-j-1]=Cr;
            }
            else
                Cr=CK[i][C-j-1];
        }
    }
    rep(j,C){
        Cr='?';
        rep(i,R){
            if(CK[i][j]=='?'){
                if(Cr!='?')
                    CK[i][j]=Cr;
            }
            else
                Cr=CK[i][j];
        }
    }
    rep(j,C){
        Cr='?';
        rep(i,R){
            if(CK[R-i-1][j]=='?'){
                if(Cr!='?')
                    CK[R-i-1][j]=Cr;
            }
            else
                Cr=CK[R-i-1][j];
        }
    }
    rep(i,R){
        rep(j,C)
            printf("%c",CK[i][j]);
        printf("\n");
    }
}
int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T;
    scanf("%d",&T);
    //cin.ignore(numeric_limits<streamsize>::max(), '\n');
    rep(n,T) {
        fprintf(stderr,"%d\n",n+1);
        printf("Case #%d:\n",n+1);
        solve();
    }
}
