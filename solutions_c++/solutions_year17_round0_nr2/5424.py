#include<cstdio>
#include<algorithm>
using namespace std;

long long n;
long long ans=0;
long long val;
void recur(int lvl,int prev){
    //printf("--> %d\n",lvl);
    if(val > n)
        return;
    if(lvl == -1){
        ans = max(ans , val);
        return ;
    }
    long long pow = 1;
    for(int i=1;i<=lvl;++i) pow*=10;
    for(int i=prev;i<=9;++i){
        val += i*pow;
        recur(lvl-1, i);
        val-= i*pow;
    }

}

int main()
{
    freopen( "B-large.in" , "r" , stdin );
    freopen( "opt.out" , "w" , stdout );
    int allt,nowt = 0;
    scanf("%d",&allt);
    while(++nowt <= allt){
        ans = 0;
        val = 0;
        printf("Case #%d: ",nowt);
        scanf("%lld",&n);
        long long i = 1;
        int a = 0;
        while(i <= n){
            i*=10,a++;
        }
        recur(a,0);
        printf("%lld\n",ans);

    }

    return 0;
}
