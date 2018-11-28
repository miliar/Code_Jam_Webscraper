#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
const double eps=1e-8;
const int mod=1e9+7;
const double pi=acos(-1.0);
const int N=1e5+5;
const int M=100;
#define INF 0x3f3f3f3f

map<int, int> a;
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d: ", ca++);
        int n, p;
        scanf("%d%d", &n, &p);
//        if(p == 2)
//        {
//            ans += (mod[1] + 1) / 2;
//        }
        a.clear();
        for(int i=0;i<n;i++)
        {
            int x;
            scanf("%d", &x);
            a[x]++;
        }
        int left=0;
        int ans=0;
        for(int i=p;i<=100;i+=p)
            if(a[i])
                ans+=a[i], a[i]=0;
        for(int i=1;i<=100;i++)
        {
            if(a[i])
            {
                if(left==0)
                    ans++;
                left=(i+left)%p;
                a[i]--;
                if(left!=0)
                {
                    for(int j=p-left;j<=100;j+=p)
                    {
                        if(a[j]!=0)
                        {
                            left=0, a[j]--;
                            break;
                        }
                    }
                }
                if(a[i])
                    i--;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}

