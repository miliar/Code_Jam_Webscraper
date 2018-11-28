#include <cstdio>
#include <map>
using namespace std;
map<long long, long long> stall;
int main()
{
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; i++)
    {
        printf("Case #%d: ", i+1);
        long long n, k;
        scanf("%lld%lld", &n, &k);
        stall.clear();
        stall[n]=1LL;
        while (true)
        {
            map<long long, long long>::iterator e=stall.end();
            e--;
            if (k<=e->second)
            {
                printf("%lld %lld", e->first/2, (e->first-1)/2);
                break; 
            }
            else
            {
                k-=e->second;
                stall[e->first/2]+=e->second;
                stall[(e->first-1)/2]+=e->second;
                stall.erase(e);
            }
        }
        printf("\n");
    }
    return 0;
}
