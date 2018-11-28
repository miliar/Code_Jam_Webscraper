#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <queue>
using namespace std;
#define read freopen("in.txt","r",stdin)
#define maxlongint 2147483647
typedef  long long LL;
typedef  unsigned long long ULL;
#pragma comment(linker, "/STACK:102400000,102400000")
#define fori for(int i=1;i<=n;i++)
#define forj for(int j=1;j<=n;j++)
#define fork for(int k=1;k<=n;k++)
#define FOR(i,n) for(int i=1;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define DREP(i,a,b) for(int i=a;i>=b;i--)
#define DOWN(i,n) for(int i=n;i>=1;i--)
#define enter cout<<endl;
#define in push_back
#define out pop_back
#define sqr(x) ((x)*(x))
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define offcin ios::sync_with_stdio(false)
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define sd(x,y) scanf("%d%d",&x,&y)
#define sch(s) scanf("%s",s)
#define fillfalse(v) memset(v,false,sizeof(v))
#define filltrue(v) memset(v,true,sizeof(v))
#define f0(a)    memset(a,0,sizeof(a))
#define Fillplus(a)    memset(a,-1,sizeof(a))
#define lowbit(x) x&(-x)
//int n,m,i,j,k,l,x,y;
int i,j,k,n,m,l,x,y,z,ans;
char s[30][30];
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int kcase=0;
    while(t--){
        int r,c;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++) scanf("%s",s[i]);
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(s[i][j]!='?'){
                    for(int k=j+1;k<c;k++)
                        if(s[i][k]!='?') break; else s[i][k]=s[i][j];
                    for(int k=j-1;k>=0;k--)
                        if(s[i][k]!='?') break; else s[i][k]=s[i][j];
                    
                }
            }
        }
        for(int i=0;i<r;i++){
            if(s[i][0]!='?'){
                for(int k=i-1;k>=0;k--)
                    if(s[k][0]!='?') break;
                        else for(int j=0;j<c;j++) s[k][j]=s[i][j];
                
                for(int k=i+1;k<r;k++)
                    if(s[k][0]!='?') break;
                        else for(int j=0;j<c;j++) s[k][j]=s[i][j];
                
            }
        }
        printf("Case #%d:\n",++kcase);
        for(int i=0;i<r;i++) printf("%s\n",s[i]);
    }
    return 0;
}
