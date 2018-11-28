#include<bits/stdc++.h>
using namespace std;
#define LEFT    0
#define RIGHT   1
//#define D(x)    //cerr << #x " = " << x << '\n'
typedef long long int LL;
LL n, k;
/// returns the level of k and the position of k in that level
pair<int,int> findLevelAndPos(LL k)
{
    pair<int,int> ret = {0,0};
    LL total = 0, currentNumOfChild = 1;
    while(true)
    {
        if(total+currentNumOfChild >= k)
        {
            k -= total;
            ret.second = k;
            return ret;
        }
        ret.first++;
        total += currentNumOfChild;
        currentNumOfChild *= 2;
    }
}



pair<LL,LL> solve(LL n, LL k)
{
    pair<int,LL> levelAndPosOfK = findLevelAndPos(k);
//    D(levelAndPosOfK.first);D(levelAndPosOfK.second);
    LL total = n - ((1<<(levelAndPosOfK.first)) - 1);
    int currentLevel = 0;
    LL x1 = n, x2 = n;
    while(currentLevel < levelAndPosOfK.first)
    {

        LL tmp = x1/2;
        if(x1%2 == 0)
            tmp--;
        x1 = tmp;
        x2 /= 2;
        currentLevel++;
    }
    LL larger = (total - (1<<levelAndPosOfK.first) *x1);
//    D(total);
//    D(larger);
    LL a, b;
    if(levelAndPosOfK.second <= larger)
    {
        a = b = x2/2;
        if(x2%2==0)
            b--;
    }
    else
    {
        a = b = x1/2;
        if(x1%2 == 0)
            b--;
    }
    return {a,b};
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
//    D(61*8);
    int i, j, cs, t;
    LL n, k;
    scanf("%d",&t);
    for(cs = 1; cs<=t; cs++)
    {
        scanf("%lld %lld",&n,&k);
//        n = 1000;
//        scanf("%lld",&k);
        printf("Case #%d: %lld %lld\n",cs,solve(n,k));
    }
}
