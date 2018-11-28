#include <bits/stdc++.h>
#define mp make_pair
#define mt make_tuple
#define X first
#define Y second
#define ALL(x) x.begin(),x.end()
#define RALL(x) x.rbegin(),x.rend()
#define D double
#define ll long long
#define REP(i,a) for(int i=0;i<a;++i)
#define REP1(i,a,b) for(int i=a;i<b;++i)
#define REP2(i,a,b) for(int i=a;i<=b;++i)
#define RREP(i,a) for(int i=a-1;i>=0;--i)
#define RREP1(i,a,b) for(int i=a;i>b;--i)
#define RREP2(i,a,b) for(int i=a;i>=b;--i)
#define SREP(i,x) for(auto i:x)
#define MS0(x) memset((x),0,sizeof((x)))
#define MS1(x) memset((x),-1,sizeof((x)))
#define MSF(x) memset((x),127,sizeof(x))
#define pb push_back
#define LE(x) (int)((x).size())
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define PDD pair<D,D>
#define im guagua
#define RI(x) x=rit()
#define RII(a,b) a=rit(),b=rit()
#define RIII(a,b,c) a=rit(),b=rit(),c=rit()
#define debug 0
const int INF = 0x7F7F7F7F;
const double EPS = 1e-10 ;
const ll mod7 = 1e9+7;
const ll mod9 = 1e9+9;
using namespace std;
inline ll rit(){
    ll f=0,key=1;
    char c;
    do{
        c=getchar();
        if(c=='-') key=-1;
    }while(c<'0' || c>'9');
    do{
        f=f*10+c-'0';
        c=getchar();
    }while(c>='0' && c<='9');
    return f*key;
}
inline void fprt(D f){
    printf("%.08lf",f);
}
void init(){
}
const int Z = 1005;
int n,rrr;
int r,b,y,rb,ry,by;
vector<string> v[3];
char ans[Z];
pair<int,char> p[3];
inline int chk(char c,int x){
    if(x==0){
        return 1;
    }
    if(x==n-2){
        if(ans[0]=='R' && r>0 && c!='R') return 0;
        if(ans[0]=='B' && b>0 && c!='B') return 0;
        if(ans[0]=='Y' && y>0 && c!='Y') return 0;
    }
    if(x==n-1){
        return c!=ans[0] && c!=ans[x-1];
    }
    return c!=ans[x-1];
}
void read(){
    RI(n);
    //
    RIII(r,ry,y);
    RIII(by,b,rb);
    p[0] = mp(r,'R');
    p[1] = mp(b,'B');
    p[2] = mp(y,'Y');
}
void solve(){
    // while(ry){
    //     if(b<2){
    //         printf("Case #%d: IMPOSSIBLE\n");
    //         return ;
    //     }
    //     ry--;
    //     b-=2;
    //     v[1].pb("BOB");
    // }
    // while(by){
    //     if(r<2){
    //         printf("Case #%d: IMPOSSIBLE\n");
    //         return ;
    //     }
    //     by--;
    //     r-=2;
    //     v[0].pb("RGR");
    // }
    // while(rb){
    //     if(y<2){
    //         printf("Case #%d: IMPOSSIBLE\n");
    //         return ;   
    //     }
    //     rb--;
    //     y-=2;
    //     v[2].pb("YVY");
    // }
    int tg=0;
    sort(p,p+3);
    REP(i,n){
        if(i*2>=n) break;
        while(p[tg].X == 0) tg++;
        ans[i*2] = p[tg].Y;
        p[tg].X--;
    }
    REP(i,n){
        if(i*2+1>=n) break;
        while(p[tg].X==0) tg++;
        ans[i*2+1] = p[tg].Y;
        p[tg].X--;
    }
    if(ans[0] == ans[n-1]){
        printf("Case #%d: IMPOSSIBLE\n",rrr);
        return ;
    }
    REP1(i,1,n){
        if(ans[i] == ans[i-1]){
            printf("Case #%d: IMPOSSIBLE\n",rrr);
        return ;       
        }
    }
    ans[n] = 0;
    printf("Case #%d: %s\n",rrr,ans);
}
int main(){
    int nn=1;
    nn=rit();
    while(nn--){
        rrr++;
        // while(cin>>n) 
            init(),read(),solve();
    }
    return 0;
}