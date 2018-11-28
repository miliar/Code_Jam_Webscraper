#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

bool check(int ans)
{
    int last=10;
    while(ans>0)
    {
        if(ans%10>last)
            return false;
        last=ans%10;
        ans/=10;
    }
    return true;
}

int counting(int N)
{
    int i=1;
    int ans=1;
    while(N>1)
    {
        if(check(N))
            break;
        N--;
    }
    return N;
}

int main()
{
    int T=0;
    scanf("%d",&T);
    for(int i=0; i<T; i++)
    {
        int n=0;
        scanf("%d",&n);
        printf("Case #%d: %d\n",i+1,counting(n));
    }
    return 0;
}
