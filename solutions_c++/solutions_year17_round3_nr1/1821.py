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
const int M = 2e4+5;
const int INF = 0x3f3f3f3f;
const int MOD = 2017;
const double pi = acos(-1.0);

struct node{
    int r,h;
    double area;
    void read(){
        scanf("%d%d",&r,&h);
        area = r*2*pi*h;
    }
}p[N],tmp[N];

bool cmp(node a,node b){
    if(a.r==b.r) return a.area>b.area;
    return a.r>b.r;
}

bool cmp1(node a,node b){
    return a.area>b.area;
}

int cas=1;
int T,n,k;

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++) p[i].read();
        sort(p,p+n,cmp);
        double best=0;
        for(int i=0;i<n;i++){
            if(i+k-1>=n) break;int u=0;
            for(int j=i+1;j<n;j++) tmp[j-i-1]=p[j],u++;
            sort(tmp,tmp+u,cmp1);
            double ans = (double)p[i].r*p[i].r*pi+p[i].area;
            for(int j=0;j<k-1;j++) ans+=tmp[j].area;
            best=max(best,ans);
        }
        printf("Case #%d: %.9f\n",cas++,best);
    }
    return 0;
}
