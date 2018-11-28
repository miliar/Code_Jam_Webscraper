#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include <limits.h>
#include<cmath>
#include<map>
#include<queue>
#include<set>
using namespace std;

#define N 100005
#define M 100005
#define LL long long

//为自己加油O(∩_∩)O~

const long long  mod =1000000007;
void gao(LL n,LL K)
{
    LL n1=1,n2=0,a=n;
    while (K>n1+n2){
        LL b=a+1;
        LL c=(a-1)/2;
        LL m1=0,m2=0;
        if (a%2==1) {
            m1+=n1*2;
            m1+=n2;m2+=n2;
        }else{
            m1+=n1;
            m2+=n2*2+n1;
        }
        K-=n1+n2;
        a=c;n1=m1;n2=m2;
    }
    if (K>n2) a--;
    LL c=a/2;
    printf("%I64d %I64d\n",a-c,c);
}
int main()
{
    freopen("Cl.in","r",stdin);
    freopen("Cl.out","w",stdout);
    int T;
    scanf("%d",&T);
    int t=T;
    while (T--){
        LL n,K;
        cin>>n>>K;
        printf("Case #%d: ",t-T);
        gao(n,K);
    }
    return 0;
}








