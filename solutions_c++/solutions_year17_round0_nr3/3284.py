#include <bits/stdc++.h>
#define fread(ch) freopen(ch,"r",stdin)
#define fwrite(ch) freopen(ch,"w",stdout)
#define Pr pair<LL,LL>

using namespace std;
using LL = long long;

priority_queue <Pr> q;

//int solve(LL k)
//{
//    int ans = 0;
//    queue <LL> q;
//    q.push(k);
//
//    while(!q.empty())
//    {
//        k = q.front();
//        q.pop();
//        while(!q.empty() && q.front() == k) q.pop();
////        printf("%lld\n",k);
//        ans++;
//
//        if(k/2 == 0) continue;
//        q.push(k/2);
//        if(k%2 == 0 && k/2-1 != 0) q.push(k/2-1);
//    }
//
//
//    return ans;
//}

int main()
{
    fread("C-large.in");
    fwrite("out.out");
    LL n,k;

    int t;

    scanf("%d",&t);

//    while(t--)
//    {
//        scanf("%lld",&k);
//        printf("%d\n",solve(k));
//    }

    for(int z = 1; z <= t; ++z)
    {
        while(!q.empty()) q.pop();
        scanf("%lld%lld",&n,&k);

        LL rest = 0,rg = 1;
        Pr tmp;
        q.push(Pr(n,1));

        while(k)
        {
            tmp = q.top();
            q.pop();

            while(!q.empty() && q.top().first == tmp.first)
            {
                tmp.second += q.top().second;
                q.pop();
            }

            if(k <= tmp.second) break;
            k -= tmp.second;

            if(tmp.first/2 == 0) continue;

            if(tmp.first%2 == 0)
            {
                if(k/2-1 != 0) q.push(Pr(tmp.first/2-1,tmp.second));
                q.push(Pr(tmp.first/2,tmp.second));
            }
            else
            {
                q.push(Pr(tmp.first/2,tmp.second*2));
            }
        }

        if(tmp.first%2 == 0) printf("Case #%d: %lld %lld\n",z,tmp.first/2,tmp.first/2-1);
        else printf("Case #%d: %lld %lld\n",z,tmp.first/2,tmp.first/2);
    }

    return 0;
}
