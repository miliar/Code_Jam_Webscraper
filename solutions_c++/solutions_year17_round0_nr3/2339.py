#include<bits/stdc++.h>
#define X first
#define Y second
#define MEM(x,y) memset(x,y,sizeof x)
using namespace std;
priority_queue<long long>pq;
unordered_map<long long,long long>mp;
void nq(long long x,long long t)
{
    if(mp[x]==0)pq.emplace(x);
    mp[x]+=t;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas;
    long long n,m,ans1,ans2,cur,tmp,ttop;
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        while(!pq.empty())pq.pop();
        mp.clear();
        cin>>n>>m;
        cur=0;
        nq(n,1);
        while(!pq.empty())
        {
            ttop=pq.top();
            tmp=mp[ttop];
            if(cur+tmp<m)
            {
                cur+=tmp;
                nq(ttop/2,tmp);
                nq(ttop-ttop/2-1,tmp);
            }
            else
            {
                printf("Case #%d: %lld %lld\n",cas,ttop/2,ttop-ttop/2-1);
                break;
            }
            pq.pop();
        }
    }
}
