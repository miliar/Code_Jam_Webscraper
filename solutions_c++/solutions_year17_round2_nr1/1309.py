#include <bits/stdc++.h>
#define fread(ch) freopen(ch,"r",stdin)
#define fwrite(ch) freopen(ch,"w",stdout)
#define LL long long
#define Pr pair<int,int>
#define VI vector<int>

using namespace std;

struct Horse
{
    int k,s;
    bool operator <(const struct Horse a)const
    {
        return k < a.k;
    }
}h[1123];

int main()
{
    fread("A-large.in");
    fwrite("out.out");

    int n,t,d;
    double ans;

    scanf("%d",&t);

    for(int z = 1; z <= t; ++z)
    {
        scanf("%d%d",&d,&n);

        ans = 0;

        for(int i = 0; i < n; ++i)
        {
            scanf("%d%d",&h[i].k,&h[i].s);
            ans = max(ans,(d-h[i].k)*1.0/h[i].s);
        }

//        printf("%f\n",ans);
        ans = d*1.0/ans;

        printf("Case #%d: %.10f\n",z,ans);
    }

    return 0;
}
