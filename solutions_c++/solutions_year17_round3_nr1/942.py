#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,j;
    int cse=1;
    int n,k;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&k);
        pair<long long int,long long int> p[n];
        for(i=0;i<n;i++)
        {
            scanf("%lld%lld",&p[i].first,&p[i].second);
        }
        sort(p,p+n);
        reverse(p,p+n);
        long long fans=0,ffans;
        for(i=0;i<=n-k;i++)
        {
            long long ans=p[i].first*p[i].second;
            priority_queue<long long> pq;
            for(j=i+1;j<n;j++)
            {
                pq.push(p[j].first*p[j].second);
            }
            int u=1;
            while(!pq.empty())
            {
                if(u==k)
                    break;
                ans+=pq.top();
                pq.pop();
                u++;
            }
            ffans=p[i].first*p[i].first+2*ans;
            fans=max(fans,ffans);
        }
        double k=((double)fans)*M_PI;
        printf("Case #%d: %lf\n",cse,k);
        cse++;
    }
    return 0;
}
