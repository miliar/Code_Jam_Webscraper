#include <bits/stdc++.h>
using namespace std;

#define INF        (~(1<<31))
#define INFLL      (~(1ll<<63))
#define pb         push_back
#define mp         make_pair
#define abs(a)     ((a)>0?(a):-(a))
#define lalal      puts("*******");
#define s1(x)      scanf("%d",&x)
#define Rep(a,b,c) for(int a=(b);a<=(c);a++)
#define Per(a,b,c) for(int a=(b);a>=(c);a--)
#define no         puts("NO")

typedef long long int LL ;
typedef unsigned long long int uLL ;

const int    MOD = 1e9+7;
const int    N   = 50000+5;
const double eps = 1e-6;
const double PI  = acos(-1.0);
void fre()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
}
inline int Rint()
{
    int x=0,f=1;
    char ch=getchar();
    while('0'>ch||ch>'9'){if(ch=='-') f=-1;ch=getchar();}
    while('0'<=ch&&ch<='0'){x=x*10+ch-'0'; ch=getchar();}
    return x*f;
}
inline LL RLL()
{
    LL x=0,f=1;
    char ch=getchar();
    while('0'>ch||ch>'9'){if(ch=='-') f=-1;ch=getchar();}
    while('0'<=ch&&ch<='0'){x=x*10+ch-'0'; ch=getchar();}
    return x*f;
}
/***********************************************************************/

int _,n,r,o,y,g,b,v;
int flag ;
void dfs(int t,string s,int m,int R,int G,int B){
//    puts("--");
    if(flag==0) return ;
    if(n==m&&flag) {
        if(s[0]!=s[n-1]){
            flag = 0;
            cout<<s<<endl;
        }
    }
    for(int i=1;i<=3&&flag;i++){
        if(i==t) continue;
        if(i==1&&R)s+="R",dfs(i,s,m+1,R-1,G  ,B  );
        if(i==2&&G)s+="G",dfs(i,s,m+1,R  ,G-1,B  );
        if(i==3&&B)s+="B",dfs(i,s,m+1,R  ,G  ,B-1);
    }
}

void dfs1(int R,int Y,int B){
    string s="";
    for(int i=1;i<=R;i++){
        s+="R";
        if(i<=Y) s+="Y";
        if(i+B>R) s+="B";
    }
//    printf("%d *1 ",s.size());
    cout<<s<<endl;
}

void dfs2(int R,int Y,int B){
    string s="";
    for(int i=1;i<=Y;i++){
        s+="Y";
        if(i<=R) s+="R";
        if(i+B>Y) s+="B";
    }
//    printf("%d *2 ",s.size());
    cout<<s<<endl;
}

void dfs3(int R,int Y,int B){
    string s="";
    for(int i=1;i<=B;i++){
        s+="B";
        if(i<=Y) s+="Y";
        if(i+R>B) s+="R";
    }
//    printf("%d *3 ",s.size());
    cout<<s<<endl;
}

int main(){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.txt","w",stdout);
    int kcase = 0;
    scanf("%d",&_);
    while(_--){
        scanf("%d",&n);

        scanf("%d%d%d%d%d%d",&r,&o,&y,&g,&b,&v);
//        printf("%d: %d %d %d %d %d %d\n",n,r,o,y,g,b,v);
        int a[4];

        a[0]=r;
        a[1]=y;
        a[2]=b;

        sort(a,a+3);printf("Case #%d: ",++kcase);
        if(a[0]+a[1]<a[2]) puts("IMPOSSIBLE");
        else {
            flag = 1;
                 if(r>=y&&r>=b) dfs1(r,y,b);
            else if(y>=r&&y>=b) dfs2(r,y,b);
            else if(b>=y&&b>=r) dfs3(r,y,b);
        }

    }

    return 0;
}
