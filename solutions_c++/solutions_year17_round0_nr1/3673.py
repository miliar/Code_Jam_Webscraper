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
const int M = 2e6+5;
const int INF = 0x3f3f3f3f;

char s[N];
int m,cas=1,T;

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    for(scanf("%d",&T);T;T--){
        scanf("%s%d",s+1,&m);
        int n=strlen(s+1);
        int ans=0;
        for(int i=1;i+m-1<=n;i++)if(s[i]=='-'){
            for(int j=i;j<=m+i-1;j++){
                if(s[j]=='+') s[j]='-';
                else s[j]='+';
            }
            ans++;
        }
        int flag=1;
        for(int i=1;i<=n;i++) flag&=(s[i]=='+');
        if(!flag) printf("Case #%d: IMPOSSIBLE\n",cas++);
        else printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
