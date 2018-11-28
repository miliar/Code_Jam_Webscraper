#pragma comment(linker, "/STACK:102400000,102400000")
#include <bits/stdc++.h>
using namespace std;
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define SZ(x) (int)(x.size())
#define rep(i,a,b) for(int i=a;i<b;i++)
#define per(i,a,b) for(int i=b-1;i>=a;i--)
#define inf 1000000007
#define mod 1000000007
#define x first
#define y second
#define pi acos(-1.0)
#define DBG(x) cerr<<(#x)<<"="<<x<<"\n";
//#define dprintf(...) 
#define hash _hash
#define next _next
//#define dprintf(...) fprintf(outFile,__VA_ARGS__)
 
#define FOREACH(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
#define ull unsigned long long
#define ll long long
#define N 200005
 
template <class T,class U>inline void Max(T &a,U b){if(a<b)a=b;}
template <class T,class U>inline void Min(T &a,U b){if(a>b)a=b;}
 
//FILE* outFile;
inline void add(int &a,int b){a+=b;while(a>=mod)a-=mod;}
 
 
int pow(int a,int b){
    int ans=1;
    while(b){
        if(b&1)ans=ans*(ll)a%mod;
        a=(ll)a*a%mod;b>>=1;
    }
    return ans;
}

char get(int k){
    if(k==0)return 'R';
    else if(k==1)return 'O';
    else if(k==2)return 'Y';
    else if(k==3)return 'G';
    else if(k==4)return 'B';
    else return 'V';
}
pii a[7];
int b[7];
int g[7][7];
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    //cerr<<setprecision(9)<<fixed;
    int T,i,j,k,ca=0,m,K,n;
    g[1][4]=g[2][5]=g[0][3]=1;
    g[4][1]=g[5][2]=g[3][0]=1;
    g[0][2]=g[2][0]=1;
    g[0][4]=g[4][0]=1;
    g[2][4]=g[4][2]=1;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%d",&n);
        m=0;
        memset(b,0,sizeof(b));
        rep(i,0,6){
            scanf("%d",&k);
            if(k)a[m++]={k,i},b[i]=k;
        }
        if(m==1){
            if(n==1){
                printf("%c\n",get(a[0].y));
            }
            else{
                puts("IMPOSSIBLE");continue;
            }
        }
        else if(m==2){
            if(a[0].x!=a[1].x||!g[a[0].y][a[1].y]){
                puts("IMPOSSIBLE");continue;
            }
            char x=get(a[0].y),y=get(a[1].y);
            rep(i,0,a[0].x){
                printf("%c%c",x,y);
            }
            puts("");
        }
        else{
            if(b[1]&&b[1]>=b[4] || b[3]&&b[3]>=b[0] || b[5]&&b[5]>=b[2]){
                puts("IMPOSSIBLE");continue;
            }
            //DBG("??")
            string s;
            vector<string>v[3];
            if(b[1]){
                s="B";rep(i,0,b[1])s=s+"OB";
                v[2].pb(s);b[4]-=b[1]+1;
            }
            rep(i,0,b[4])v[2].pb("B");
            if(b[3]){
                s="R";rep(i,0,b[3])s=s+"GR";
                v[1].pb(s);b[0]-=b[3]+1;
            }
            rep(i,0,b[0])v[1].pb("R");
            if(b[5]){
                s="Y";rep(i,0,b[5])s=s+"VY";
                v[0].pb(s);b[2]-=b[5]+1;
            }
            rep(i,0,b[2])v[0].pb("Y");
            a[0]={SZ(v[0]),0},a[1]={SZ(v[1]),1},a[2]={SZ(v[2]),2};
            sort(a,a+3);
            K=a[0].x+a[1].x-a[2].x;
            if(K<0){
                puts("IMPOSSIBLE");continue;
            }
            int x=a[0].y,y=a[1].y,z=a[2].y;
            rep(i,0,K){
                cout<<v[z][i]<<v[x][i]<<v[y][i];
            }
            m=K;
            rep(i,K,a[0].x)cout<<v[z][m++]<<v[x][i];
            rep(i,K,a[1].x)cout<<v[z][m++]<<v[y][i];
            puts("");
        }
    }
    //cerr<<clock()*1./CLOCKS_PER_SEC<<"ms\n";
    return 0;
} 