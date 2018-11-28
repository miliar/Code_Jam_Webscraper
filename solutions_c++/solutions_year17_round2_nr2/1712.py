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

int a[5],cas=1;
int pre[N],nxt[N],tot,val[N];

void link(int u,int v){
    pre[v]=u;
    nxt[u]=v;
}
char id[3]={'R','Y','B'};
int T,n;
void display(){
    int flag=1;
    for(int now=0;flag||now;now=nxt[now]){
        cout<<id[val[now]];
        flag=0;//cout<<now<<' '<<nxt[now]<<endl;
    }cout<<endl;
}
int main(){
    //freopen("B-small-attempt1.in","r",stdin);
    //freopen("B-small-attempt1.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        int maxv=-INF,mx;
        int minv=INF,mv;
        for(int i=0,t;i<3;i++){
            scanf("%d%d",&a[i],&t);
            if(a[i]>maxv) maxv=a[i],mx=i;
        }
        for(int i=0;i<3;i++) if(a[i]<minv&&i!=mx) minv=a[i],mv=i;
        if(maxv*3<n||maxv*2>n){
            printf("Case #%d: IMPOSSIBLE\n",cas++);
            continue;
        }
        //cout<<minv<<' '<<maxv<<' '<<mx<<' '<<mv<<endl;
        tot=0;
        val[tot++]=mx;
        for(int i=1;i<maxv;i++){
            val[tot]=mx;
            //cout<<tot-1<<' '<<tot<<endl;
            link(tot-1,tot);tot++;
        }
        link(tot-1,0);//cout<<tot<<endl;
        //display();
        int now=0;//cout<<minv
        for(int i=0;i<minv;i++){
            val[tot]=mv;
            link(tot,nxt[now]);link(now,tot);
            now=nxt[tot++];
        }//cout<<'a';
        int left=n-minv-maxv;
        for(int i=0;i<left;i++){
            val[tot]=3-mx-mv;
            link(tot,nxt[now]);link(now,tot);
            now=nxt[tot++];
        }
        printf("Case #%d: ",cas++);
        for(int i=0,now=0;i<n;i++,now=nxt[now]) printf("%c",id[val[now]]);printf("\n");
    }
    return 0;
}
/*
1
468 75 0 182 0 211 0
*/
