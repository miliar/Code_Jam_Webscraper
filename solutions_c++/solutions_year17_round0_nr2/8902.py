#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
using namespace std;

const int MAXN=1000;

bool isTidy(int a)
{
    if (a<10) return true;
    int last=a%10;
    a/=10;
    while (a>0){
        if (a%10>last) return false;
        last=a%10;
        a/=10;
    }
    return true;
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B_output_small.txt","w",stdout);
    int T,N;
    bool tidy[1001];
    memset(tidy,0,sizeof(tidy));
    for (int i=1;i<=1000;i++){
        tidy[i]=isTidy(i);
    }
    scanf("%d",&T);
    for (int index=1;index<=T;index++)
    {
        scanf("%d",&N);
        int ans=0;
        for (int i=N;i>=1;i--)
        {
            if (tidy[i]) {ans=i; break;}
        }
        printf("Case #%d: %d\n",index,ans);
    }
    return 0;
}
