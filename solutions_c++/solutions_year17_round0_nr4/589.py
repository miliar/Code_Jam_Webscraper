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
#define N 100010
 
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

const int M=100;
int a[105][105],n,b[105][105],r[105],c[105],d[205],f[205],sz,ans,tot;
struct node{
    int x,y,t;
}res[10010],v[10010];
void dfs(){
    int s=0;vector<pii>his;
    rep(i,0,n){
        rep(j,0,n){
            if(a[i][j]!=-1){s+=(a[i][j]?1:2);continue;}
            if(a[i][j]==-1){
                if(r[i]+c[j]==0){
                    his.pb({i,j});
                    r[i]=c[j]=1;
                    res[sz++]={i,j,2};
                    s+=1;
                }
            }
        }
    }
    while(!his.empty()){
        pii e=his.back();his.pop_back();
        r[e.x]=c[e.y]=0;
    }
    if(s>ans){
        ans=s;
        rep(i,0,sz)v[i]=res[i];
        tot=sz;
    }
}
void dfs(int x,int y,int s=0){
    if(x==n){
        ans=s;return;
    }
    if(y==n){
        dfs(x+1,0,s);return;
    }
    if(a[x][y]==0){
        dfs(x,y+1,s+2);return;
    }
    if(a[x][y]==1){
        if(r[x]+c[y]==0){
            r[x]=c[y]=1;
            v[sz++]={x,y,0};
            dfs(x,y+1,s+2);
            return;
        }
        dfs(x,y+1,s+1);
    }
    else if(a[x][y]==2){
        if(d[x-y+M]+f[x+y]==0){
            d[x-y+M]=f[x+y]=1;
            v[sz++]={x,y,0};
            dfs(x,y+1,s+2);
            return;
        }
        dfs(x,y+1,s+1);
    }
    else{
        if(r[x]+c[y]+d[x-y+M]+f[x+y]==0){
            r[x]=c[y]=1;d[x-y+M]=f[x+y]=1;
            v[sz++]={x,y,0};
            dfs(x,y+1,s+2);
            return;
        }
        if(d[x-y+M]+f[x+y]==0){
            d[x-y+M]=f[x+y]=1;
            v[sz++]={x,y,1};
            dfs(x,y+1,s+1);
            return;
        }
        if(r[x]+c[y]==0){
            r[x]=c[y]=1;
            v[sz++]={x,y,2};
            dfs(x,y+1,s+1);
            return;
        }
        dfs(x,y+1,s);
    }
}
int main(){
    freopen("A.in","r",stdin);
    freopen("B.out","w",stdout);
    //cout<<setprecision(9)<<fixed;
    int T,i,j,k,ca=0,m,K;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%d%d",&n,&m);
        //cerr<<n<<" "<<m<<"??\n";
        rep(i,0,n+1)rep(j,0,n+1)a[i][j]=-1;
        rep(i,0,n)r[i]=c[i]=0;
        rep(i,0,n)rep(j,0,n){
            d[i-j+M]=f[i+j]=0;
        }
        int flag=0;
        rep(i,0,m){
            getchar();char cc;
            scanf("%c%d%d",&cc,&j,&k),j--,k--;
            K=a[j][k]=cc=='o'?0:(cc=='+'?1:2);
            if(K==0||K==1)d[j-k+M]=f[j+k]=1;
            if(K==0||K==2)r[j]=c[k]=1;
            if(K==0)flag=1;
        }
        rep(i,0,n)rep(j,0,n)b[i][j]=a[i][j];
        rep(i,0,n)if(a[0][i]==-1&&d[0-i+M]==0&&f[i]==0)a[0][i]=d[0-i+M]=f[i]=1;
        rep(i,0,n)if(a[i][n-1]==-1&&d[i-n+1+M]==0&&f[i+n-1]==0)a[i][n-1]=d[i-n+1+M]=f[i+n-1]=1;
        rep(i,0,n)if(a[n-1][i]==-1&&d[n-1-i+M]==0&&f[i+n-1]==0)a[n-1][i]=d[n-1-i+M]=f[i+n-1]=1;
        rep(i,0,n)if(a[i][0]==-1&&d[i+M]==0&&f[i]==0)a[i][0]=d[i+M]=f[i]=1;
        ans=0;sz=0;
        dfs(0,0);tot=sz;
        // if(!flag)
        // rep(i,0,n)rep(j,0,n){
        //     if(a[i][j]==1&&r[i]==0&&c[j]==0){
        //         r[i]=c[j]=1;sz=0;
        //         res[sz++]={i,j,0};
        //         a[i][j]=0;
        //         dfs();
        //         r[i]=c[j]=0;a[i][j]=1;
        //         //break;
        //     }
        //     if(a[i][j]==2&&d[i-j+M]==0&&f[i+j]==0){
        //         d[i-j+M]=f[i+j]=1;sz=0;
        //         res[sz++]={i,j,0};
        //         a[i][j]=0;
        //         dfs();
        //         d[i-j+M]=f[i+j]=0;a[i][j]=2;
        //     }
        //     if(a[i][j]==-1&&d[i-j+M]==0&&f[i+j]==0&&r[i]==0&&c[j]==0){
        //         r[i]=c[j]=1;d[i-j+M]=f[i+j]=1;sz=0;
        //         res[sz++]={i,j,0};
        //         a[i][j]=0;
        //         dfs();
        //         sz--;
        //         r[i]=c[j]=0;d[i-j+M]=f[i+j]=0;a[i][j]=-1;
        //     }
        // }
        rep(i,0,tot)a[v[i].x][v[i].y]=v[i].t;
        sz=0;
        rep(i,0,n)rep(j,0,n)if(a[i][j]!=b[i][j]){
            v[sz++]={i,j,a[i][j]};
        }
        printf("%d %d\n",ans,sz);
        
        rep(i,0,sz){
            printf("%c %d %d\n",v[i].t==0?'o':(v[i].t==1?'+':'x'),v[i].x+1,v[i].y+1);
        }//*/
    }
    //cerr<<clock()*1./CLOCKS_PER_SEC<<"ms\n";
    return 0;
}