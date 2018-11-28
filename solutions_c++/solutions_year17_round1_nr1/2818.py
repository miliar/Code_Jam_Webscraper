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

const int N = 15;
const int M = 27;
const int INF = 0x3f3f3f3f;

char s[N][N],b[N][N];
int lx[M],ly[M],rx[M],ry[M],used[M];
int cas=1,T,r,c,cnt,ok;

void debug(){
    for(int i=1;i<=r;i++) cout<<b[i]+1<<endl;cout<<cnt<<endl;
}
int nn=0;
void dfs(int i){
    if(ok||i>=26) return;
    if(!used[i]){
        dfs(i+1);
        return;
    }
    //if(nn++>=5) return;
    //cout<<i;
    //debug();cout<<endl;
    if(!cnt){
        ok=1;
        for(int i=1;i<=r;i++){
            for(int j=1;j<=c;j++) printf("%c",b[i][j]);
            printf("\n");
        }
        return;
    }
    if(ly[i]>1){
        int flag=1;
        for(int k=rx[i];k<=lx[i];k++) flag&=(b[k][ly[i]-1]=='?');
        if(flag){
            for(int k=rx[i];k<=lx[i];k++) b[k][ly[i]-1]=i+'A',cnt--;
            ly[i]--;//cout<<'a';
            dfs(i);
            for(int k=rx[i];k<=lx[i];k++) b[k][ly[i]-1]=s[k][ly[i]-1],cnt++;
            ly[i]++;
        }
    }
    if(ry[i]<c){
        int flag=1;
        for(int k=rx[i];k<=lx[i];k++) flag&=(b[k][ry[i]+1]=='?');
        if(flag){
            for(int k=rx[i];k<=lx[i];k++) b[k][ry[i]+1]=i+'A',cnt--;
            ry[i]++;//cout<<'b';
            dfs(i);
            for(int k=rx[i];k<=lx[i];k++) b[k][ry[i]+1]=s[k][ry[i]+1],cnt++;
            ry[i]--;
        }
    }
    //debug();return 0;
    if(rx[i]>1){
        int flag=1;
        for(int k=ly[i];k<=ry[i];k++) flag&=(b[rx[i]-1][k]=='?');
        if(flag){
            for(int k=ly[i];k<=ry[i];k++) b[rx[i]-1][k]=i+'A',cnt--;
            rx[i]--;//cout<<'c';
            dfs(i);
            for(int k=ly[i];k<=ry[i];k++) b[rx[i]-1][k]=s[rx[i]-1][k],cnt++;
            rx[i]++;
        }
    }
    if(lx[i]<r){
        int flag=1;
        for(int k=ly[i];k<=ry[i];k++) flag&=(b[lx[i]+1][k]=='?');
        if(flag){
            for(int k=ly[i];k<=ry[i];k++) b[lx[i]+1][k]=i+'A',cnt--;
            lx[i]++;//cout<<'d';//debug();
            dfs(i);
            for(int k=ly[i];k<=ry[i];k++) b[lx[i]+1][k]=s[lx[i]+1][k],cnt++;
            lx[i]--;
        }
    }
    dfs(i+1);
}

int main(){
    //freopen("A-small-attempt3.in","r",stdin);
    //freopen("A-small-attempt3.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        for(int i=0;i<26;i++) lx[i]=ry[i]=-INF,ly[i]=rx[i]=INF,used[i]=0;
        scanf("%d%d",&r,&c);
        for(int i=1;i<=r;i++) scanf("%s",s[i]+1);
        //debug();
        cnt=0;
        for(int i=1;i<=r;i++)
        for(int j=1;j<=c;j++) {
            if(s[i][j]!='?'){
                int c=s[i][j]-'A';used[c]++;
                //cout<<s[i][j]<<' '<<c<<endl;
                lx[c]=max(lx[c],i);ly[c]=min(ly[c],j);
                rx[c]=min(rx[c],i);ry[c]=max(ry[c],j);
            }else cnt++;
        }
        for(int i=0;i<26;i++)if(used[i]){
            for(int x=rx[i];x<=lx[i];x++)
            for(int y=ly[i];y<=ry[i];y++) s[x][y]=i+'A';
        }
        //for(int i=1;i<=r;i++) cout<<s[i]+1<<endl;
        //return 0;
        printf("Case #%d:\n",cas++);
        ok=0;
        for(int i=0;i<26;i++) if(!ok&&used[i]){
            for(int x=1;x<=r;x++)
            for(int y=1;y<=c;y++) b[x][y]=s[x][y];
            dfs(i);
        }

        //for(int i=1;i<=r;i++) printf("%s\n",s[i]+1);
    }
    return 0;
}
/*
3
3 4
AC??
???E
B?DF
*/
