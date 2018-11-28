#include <bits/stdc++.h>

#define MAX 100000
#define INF 2000000000

typedef long long ll;
typedef unsigned long long llu;

using namespace std;

void IO()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
}

llu n,maxn;

void Fun(llu num)
{
    if(num>n)return;
    maxn=max(maxn,num);
    llu d=(num%10==0)?1:num%10;
    for(llu i=d;i<=9;i++){
        Fun((num*10)+i);
    }
}

int main()
{
    //IO();
    llu t;
    scanf("%llu",&t);
    for(llu i=1;i<=t;i++){
        scanf("%llu",&n);
        printf("Case #%llu: ",i);
        if(n<10){
            printf("%llu\n",n);
            continue;
        }
        maxn=0;
        Fun(0);
        printf("%llu\n",maxn);
    }
    return 0;
}
