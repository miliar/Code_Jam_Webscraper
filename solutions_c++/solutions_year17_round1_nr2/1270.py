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
#define N 300010
 
template <class T,class U>inline void Max(T &a,U b){if(a<b)a=b;}
template <class T,class U>inline void Min(T &a,U b){if(a>b)a=b;}
 
//FILE* outFile;
inline void add(int &a,int b){a+=b;if(a>=mod)a-=mod;}


int pow(int a,int b){
    int ans=1;
    while(b){
        if(b&1)ans=ans*(ll)a%mod;
        a=(ll)a*a%mod;b>>=1;
    }
    return ans;
}


int n,m,c[55],a[55],dp[55][55];
pii b[55][55];
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    //cout<<setprecision(9)<<fixed;
    //cerr<<setprecision(9)<<fixed;
    int T,i,j,k,ca=0,K;
    scanf("%d",&T);
    rep(ca,1,T+1){
        printf("Case #%d: ",ca);
        scanf("%d%d",&n,&m);
        rep(i,0,n)scanf("%d",&a[i]);
        int ans=0;
        rep(i,0,n){
            rep(j,0,m){
                scanf("%d",&c[j]);
            }
            sort(c,c+m);
            rep(j,0,m){
                k=c[j];
                //DBG(k)
                int r=k/(a[i]*0.9),l=ceil(k/(a[i]*1.1));
                if(l<=0)l=1;
                //cerr<<l<<" "<<r<<"\n";
                b[i][j]={l,r};
                if(n==1&&l<=r)ans++;
            }
        }
        memset(dp,0,sizeof(dp));
        rep(i,0,m){
            rep(j,0,m){
                Max(dp[i+1][j],dp[i][j]);
                if(b[0][i].x<=b[0][i].y){
                    rep(k,j,m){
                        if(b[1][k].x<=b[1][k].y){
                            int x1=b[1][k].x,y1=b[1][k].y,x2=b[0][i].x,y2=b[0][i].y;
                            //DBG("??")
                            if(x2<=y1&&x2>=x1 || y2>=x1&&y2<=y1){
                                //cerr<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<"\n";
                                Max(dp[i+1][k+1],1+dp[i][j]);
                                break;
                            }
                        }
                    }
                }
            }
        }
        
        rep(i,0,m+1)Max(ans,dp[m][i]);
        printf("%d\n",ans);
    }
    //cerr<<clock()*1./CLOCKS_PER_SEC<<"ms\n";
    return 0;
}