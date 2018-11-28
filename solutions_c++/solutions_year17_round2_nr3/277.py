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

double dp[105][105],w[105][105];
int vis[105],in[105],n;
pii a[105];
void cal(int s,double d[]){
    queue<int>q;q.push(s);
    rep(i,0,n)d[i]=-1,in[i]=0;d[s]=0;
    while(!q.empty()){
        int u=q.front();q.pop();in[u]=0;
        rep(i,0,n){
            if(w[u][i]>=0&&w[u][i]<=a[u].x){
                if(d[i]==-1||d[i]>d[u]+w[u][i]/a[u].y){
                    d[i]=d[u]+w[u][i]/a[u].y;
                    if(!in[i])in[i]=1,q.push(i);
                }
            }
        }
    } 
}
double cal(int s,int t){
    if(vis[s])return dp[s][t];
    vis[s]=1;
    cal(s,dp[s]);
    return dp[s][t];
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    //cerr<<setprecision(9)<<fixed;
    int T,i,j,k,ca=0,m,K;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%d%d",&n,&m);
        rep(i,0,n)scanf("%d%d",&a[i].x,&a[i].y),vis[i]=0;
        rep(i,0,n){
            rep(j,0,n)scanf("%lf",&w[i][j]);
        }
        rep(k,0,n){
            rep(i,0,n){
                rep(j,0,n){
                    if(w[i][k]>=0&&w[k][j]>=0){
                        if(w[i][j]<0||w[i][j]>w[i][k]+w[k][j]){
                            w[i][j]=w[i][k]+w[k][j];
                        }
                    }
                }
            }
        }
        rep(i,0,m){
            int s,t;
            scanf("%d%d",&s,&t),s--,t--;
            printf("%lf ",cal(s,t));
        }
        puts("");
    }
    //cerr<<clock()*1./CLOCKS_PER_SEC<<"ms\n";
    return 0;
} 