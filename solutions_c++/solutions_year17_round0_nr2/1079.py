#include<cstdio>
#include<algorithm>
#include<cstdlib>

using namespace std;

const int MAXN=20;
int N;
int T;
int kase=0;
int a[MAXN];


inline int Min(int a,int b)
{
    return a>b?a:b;
}
inline void case_init()
{
    printf("Case #%d: ",++kase);
    char t=getchar();
    while(t<'0'||t>'9') t=getchar();
    for(N=0;t<='9'&&t>='0';t=getchar()) a[++N]=t-'0';
}
inline void case_solve()
{
/*
    for(int i=N;i;--i)
        for(int j=i;j;--j)
            a[j]=Min(a[j],a[i]);

    printf("Case #%d: ",++kase);
    if(a[1]==0)
        for(int i=1;i<N;++i) putchar('9');
    else
        for(int i=1;i<=N;++i) putchar('0'+a[i]);
    putchar('\n');
*/
//    for(int i=1;i<=N;++i) printf("%d",a[i]);
//    putchar('\n');
    int amin;
    int i,j;
    if(N==1)
    {
        putchar(a[1]+'0');putchar('\n');
        return ;
    }
    for(i=1;i<N;++i) if(a[i+1]<a[i]) break;
    if(i==N)
    {
        for(int i=1;i<=N;++i) putchar('0'+a[i]);
        putchar('\n');
        return ;
    }
    for(j=i+1;j<=N;++j) a[j]=9;
    for(;i;--i)
    {
        --a[i];
        if(a[i]>=a[i-1]) break;
        a[i]=9;
    }
    for(i=1;i<=N;++i) if(a[i]) break;
    for(;i<=N;++i) putchar('0'+a[i]);
    putchar('\n');
/*
    for(j=i+1,amin=a[i];j<=N;++j) if(a[j]<amin) amin=a[j];
    if(amin==0)
    {
        for(int i=1;i<N;++i) putchar('9');
        putchar('\n');
        return ;
    }
    for(i=1;i<=N;++i)
    {
        if(a[i]>amin) break;
        putchar('0'+a[i]);
    }
    putchar('0'+amin);
    for(++i;i<=N;++i) putchar('9');
    putchar('\n');
*/
    return ;
}
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    for(scanf("%d",&T);T;--T)
    {
        case_init();
        case_solve();
//        printf("%d   ",N);
//        for(int i=1;i<=N;++i) putchar('0'+a[i]);
//        putchar('\n');
    }
    return 0;
}
