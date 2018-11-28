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

pair<double,int> a[1005];
struct node{
    double t,x,v;
};
vector<node>q;
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    //cerr<<setprecision(9)<<fixed;
    int T,i,j,k,ca=0,m,K,n;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%d%d",&K,&n);
        rep(i,0,n){
            scanf("%lf%d",&a[i].x,&a[i].y);
        }
        sort(a,a+n);
        a[n]={K+1,inf};
        int x=n-1;
        rep(i,0,n-1){
            if(a[i].y<=a[i+1].y){x=i;break;}
        }
        double t;
        q.clear();
        q.pb({0,a[0].x,a[0].y});
        double l=a[x].y,r=1e15;
        while(x>=0&&a[0].x<K){
            double mi=1.*(K-a[x].x)/a[x].y;
            rep(i,0,x){
                t=1.*(a[i+1].x-a[i].x)/(a[i].y-a[i+1].y);
                if(t<mi)mi=t;
            }
            //DBG(mi)
            rep(i,0,x+1){
                a[i].x+=a[i].y*mi;
            }
            while(x>=0&&a[x].x==K)x--;
            if(x<0){
                q.pb({mi,a[0].x,a[0].y});break;
            }
            m=0;a[m++]=a[x];
            per(i,0,x)if(a[i].x<a[m-1].x)a[m++]=a[i];
            reverse(a,a+m);
            x=m-1;
            q.pb({mi,a[0].x,a[0].y});
        }
        for(auto o:q){
            //cerr<<o.x<<" "<<o.t<<" "<<o.v<<"\n";
        }
        rep(c,0,200){
            double v=(l+r)/2,pos=0;int ok=1;
            rep(i,0,SZ(q)-1){
                t=q[i+1].t;
                if(v<=q[i].v){
                    pos+=v*t;
                }
                else{
                    double t1=(q[i].x-pos)/(v-q[i].v);
                    if(t1<t){ok=0;break;}
                    pos+=v*t;
                }
            }
            if(ok)l=v;
            else r=v;
        }
        printf("%lf\n",(l+r)/2);
    }
    //cerr<<clock()*1./CLOCKS_PER_SEC<<"ms\n";
    return 0;
} 