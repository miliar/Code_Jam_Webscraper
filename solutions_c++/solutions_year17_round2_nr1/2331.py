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

int main()
{
    freopen("22.in","r",stdin);
    freopen("2.out","w",stdout);
    int T;
    scanf("%d",&T);
    int t=T;
    while (T--){
        int D,n;
        scanf("%d%d",&D,&n);
        double ans=1e60;
        int k,s;
        for (int j=0;j<n;j++){
            scanf("%d%d",&k,&s);
            ans=min(ans,D*1.0/(D-k)*s);
        }
        printf("Case #%d: %.6f\n",t-T,ans);
    }
    return 0;
}








