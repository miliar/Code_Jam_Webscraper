#include"iostream"
#include"cstring"
#include"cstdio"
#include"queue"
#include"set"
#include"map"
#include"algorithm"
#include"cmath"
#define clr(a) memset(a,0,sizeof(a))
#define mdzz int mid=(L+R)>>1;
#define ls pos<<1
#define rs pos<<1|1
#define lson L,mid,ls
#define rson mid+1,R,rs
#define fr first
#define sc second
using namespace std;

typedef long long LL;

const int N = 1e3+5;
const int M = 105;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9+7;

struct node{
    double x,v;
}p[N];

bool cmp(node a,node b){
    return a.x<b.x;
}

int f[N];

int fa(int x){
    return x==f[x]?x:f[x]=fa(f[x]);
}
int T,cas=1,n;
double d;

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%lf%d",&d,&n);
        p[n].x=d;p[n].v=0;f[n]=n;
        for(int i=0;i<n;i++) scanf("%lf%lf",&p[i].x,&p[i].v),f[i]=i;
        sort(p,p+n,cmp);
        double cur=0;
        for(int k=0;k<n;k++){
            double minv = 1e18;
            int pos=-1;
            for(int i=0;i<n;i++) if(fa(i)==i&&p[i].v>p[fa(i+1)].v){
                double cost = (p[fa(i+1)].x-p[i].x)/(p[i].v-p[fa(i+1)].v);
                //cout<<p[fa(i+1)].v<<' '<<p[i].v<<' '<<cost<<endl;
                if(cost<minv) minv=cost,pos=i;
            }//cout<<pos<<' '<<minv<<endl;
            if(pos==-1) break;
            if(fabs(p[fa(0)].x+p[fa(0)].v*minv-d)<1e-6) break;//cout<<p[fa(0)].x+p[fa(0)].v*minv<<' '<<d<<endl;
            f[pos]=fa(pos+1);//cout<<fa(0)<<endl;
            for(int i=0;i<n;i++) if(fa(i)==i){
                p[i].x+=p[i].v*minv;
                //cout<<i<<' '<<p[i].x<<endl;
            }
            cur+=minv;
        }
        //cout<<p[fa(0)].x<<endl;
        cur+=(d-p[fa(0)].x)/p[fa(0)].v;
        printf("Case #%d: %.6f\n",cas++,d/cur);
    }
    return 0;
}
