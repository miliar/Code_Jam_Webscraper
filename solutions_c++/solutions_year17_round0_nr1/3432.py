#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int cases, n, ans, len;
char pan[1010];
int cake[1010];

void Init()
{
    memset(pan,0,sizeof(pan));
    scanf("%s",pan);
    scanf("%d",&n);
    len=strlen(pan);
    for(int i=0;i<len;++i){
        if(pan[i]=='+')
            cake[i]=0;
        else cake[i]=1;
    }
    ans=0;
}

void Solve()
{
    int i=0;
    for(;i+n<=len;++i){
        if(cake[i]){
            ++ans;
            for(int j=0;j<n;++j)
                cake[i+j]=1-cake[i+j];
        }
    }
    while(i<len){
        if(cake[i]){
            printf("IMPOSSIBLE\n");
            return;
        }
        ++i;
    }
    printf("%d\n",ans);
}

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("a.out","w",stdout);

    scanf("%d",&cases);
    for(int kase=1;kase<=cases;++kase){
        printf("Case #%d: ",kase);
        Init();
        Solve();
    }
    return 0;
}

