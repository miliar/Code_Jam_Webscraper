// GCJ2017 qua round 2017/04/08
// problem B tidy number
// ELCT
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int cases, len;
int num[25];
char raw[25];

void Init()
{
    memset(raw, 0, sizeof(raw));
    scanf("%s",raw);
    len=strlen(raw);
    for(int i=0;i<len;++i)
        num[i]=raw[i]-'0';
    num[len]=9;
}

void Solve()
{
    int last=0;
    while(last<len-1){
        if(num[last]<=num[last+1])
            ++last;
        else break;
    }
    if(last<len-1){
        --num[last];  // never be zero
        for(int i=last+1;i<len;++i)
            num[i]=9;
        for(int i=last;i>0;--i){
            if(num[i]<num[i-1]){
                num[i]=9;
                --num[i-1];
            }
            else break;
        }

    }

    int i=0;
    while(!num[i]) ++i;
    for(;i<len;++i)
        if(num[i])
        printf("%d",num[i]);
    printf("\n");
}

int main()
{
    // don't forget to comments these
    //freopen("B-large.in","r",stdin);
    //freopen("b.out","w",stdout);
    // don't forget to comments these

    scanf("%d",&cases);
    for(int kase=1;kase<=cases;++kase){
        printf("Case #%d: ",kase);
        Init();
        Solve();
    }
    return 0;
}
