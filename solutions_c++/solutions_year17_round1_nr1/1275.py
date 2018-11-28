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


char s[30][30];
bool check_r(int x,int l,int r){
    rep(i,l,r+1)if(s[x][i]!='?')return 0;
    return 1;
}
bool check_c(int y,int l,int r){
    rep(i,l,r+1)if(s[i][y]!='?')return 0;
    return 1;
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    //cout<<setprecision(9)<<fixed;
    //cerr<<setprecision(9)<<fixed;
    int T,i,j,k,ca=0,m,K,n;
    scanf("%d",&T);
    rep(ca,1,T+1){
        printf("Case #%d:\n",ca);
        scanf("%d%d",&n,&m);
        rep(i,0,n)scanf("%s",s[i]);
        pii x[26],y[26];
        rep(i,0,26){
            x[i]=y[i]={inf,-1};
        }
        rep(i,0,n){
            rep(j,0,m)if(s[i][j]!='?'){
                k=s[i][j]-'A';
                Max(x[k].y,i),Min(x[k].x,i);
                Max(y[k].y,j),Min(y[k].x,j);
            }
        }
        rep(i,0,n){
            rep(j,0,m)if(s[i][j]=='?'){
                rep(k,0,26)if(i>=x[k].x&&i<=x[k].y&&j>=y[k].x&&j<=y[k].y){
                    s[i][j]=k+'A';
                }
            }
        }
        queue<int>q;
        rep(t,0,100){
        int vis[26]={0};
        rep(i,0,n)rep(j,0,m)if(s[i][j]!='?'){
            k=s[i][j]-'A';
            if(vis[k])continue;
            vis[k]=1;
            int x1=x[k].x,x2=x[k].y,y1=y[k].x,y2=y[k].y;
            while(y1&&check_c(y1-1,x1,x2)){
                rep(l,x1,x2+1)s[l][y1-1]=k+'A';
                y1--;
            }
            while(x1&&check_r(x1-1,y1,y2)){
                rep(l,y1,y2+1)s[x1-1][l]=k+'A';
                x1--;
            }
            while(y2<m-1&&check_c(y2+1,x1,x2)){
                rep(l,x1,x2+1)s[l][y2+1]=k+'A';
                y2++;
            }
            while(x2<n-1&&check_r(x2+1,y1,y2)){
                rep(l,y1,y2+1)s[x2+1][l]=k+'A';
                x2++;
            }
            
            //cerr<<x1<<" "<<x2<<" "<<y1<<" "<<y2<<"\n";
        }
        int ok=1;
        rep(i,0,n){
            rep(j,0,m)if(s[i][j]=='?')ok=0;
        }
        if(ok)break;
        }
        rep(i,0,n){
            rep(j,0,m)if(s[i][j]=='?')DBG(0)
        }
        rep(i,0,n)puts(s[i]);
    }
    //cerr<<clock()*1./CLOCKS_PER_SEC<<"ms\n";
    return 0;
}