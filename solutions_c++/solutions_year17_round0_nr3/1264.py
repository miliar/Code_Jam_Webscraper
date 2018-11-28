#include<bits/stdc++.h>
using namespace std;
long long n,k;
map<long long,long long> cnt;
vector<long long> p;
void f(long long x,long long y)
{
    if(x<=0) return ;
    if(cnt[x]==0) p.push_back(x);
    cnt[x] += cnt[y];
}
main()
{
    int time,cnum=1;
    int i;
    long long x,l,r,sum;
    freopen("C-large.in","r",stdin);
    freopen("C_out.txt","w",stdout);
    scanf("%d",&time);
    while(time--)
    {
        cerr << time << endl;
        scanf("%lld%lld",&n,&k);
        p.clear(); cnt.clear();
        cnt[n] = 1;
        p.push_back(n);
        sum = 0;
        for(i=0;i<p.size();i++)
        {
            x = p[i];
            sum += cnt[x];
            if(sum>=k)
            {
                if(x%2==0)
                {
                    l = x/2-1;
                    r = x/2;
                }
                else l = r = (x-1)/2;
                printf("Case #%d: %lld %lld\n",cnum++,max(l,r),min(l,r));
                break;
            }
            if(x%2==0)
            {
                f(x/2,x);
                f(x/2-1,x);
            }
            else
            {
                f((x-1)/2,x);
                f((x-1)/2,x);
            }
        }
    }
}
