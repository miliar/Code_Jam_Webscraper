#include <cstdio>
#include <algorithm>

using namespace std;

inline bool check(int val)
{
    int last=10;
    while (val)
    {
        if (val%10>last)
            return false;
        last=val%10;
        val/=10;
    }
    return true;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int itr=1; itr<=tc; itr++)
    {
        int n;
        scanf("%d",&n);
        while (!check(n))
        {
            n--;
        }
        printf("Case #%d: %d\n",itr,n);
    }
}
