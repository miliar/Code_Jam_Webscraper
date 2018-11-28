#include <bits/stdc++.h>
using namespace std;
struct rg
{
    int l,r;
    int md;
    int mn;
    int mx;
    rg(int ll,int rr): l(ll),r(rr)
    {
        md=(l+r)/2;
        mn=min(r-1-md,md-l-1);
        mx=max(r-1-md,md-l-1);
    }

};
bool cmp(const rg&a,const rg&b)
{
    if(a.mn==b.mn)
    {
        if(a.mx==b.mx)
        {
            return a.md>b.md;
        }
        return a.mx<b.mx;
    }
    return a.mn<b.mn;
}
vector<rg> rs;
int main()
{
    freopen("C2.in","r",stdin);
    freopen("C.out","w",stdout);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        long long n,k;
        cin>>n>>k;
        rs.clear();
        rs.push_back(rg(0,n+1));
        int o1=0;
        int o2=0;
        while(k!=0)
        {
            rg m=rs[0];
            pop_heap(rs.begin(),rs.end(),cmp);
            rs.pop_back();
            //cout<<m.l<<" "<<m.r<<" "<<m.md<<" "<<m.mn<<" "<<m.md<<endl;
            rg a1=rg(m.l,m.md);
            rg a2=rg(m.md,m.r);
            o1=m.mn;
            o2=m.mx;
            rs.push_back(a1);
            push_heap(rs.begin(),rs.end(),cmp);
            rs.push_back(a2);
            push_heap(rs.begin(),rs.end(),cmp);
            k--;
        }
        printf("Case #%d: %d %d\n",tt,o2,o1);

    }
}
