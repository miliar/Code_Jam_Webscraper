#include<bits/stdc++.h>
using namespace std;
#define lli long long int
#define mp make_pair
class ComparisonClass 
{
	public:
    bool operator() (pair<lli,lli>a,pair<lli,lli>b) 
	{
        return a.first<b.first;
    }
};
int main()
{
	freopen("C-large.in","r",stdin);
    freopen("Cout3.out","w",stdout);
    lli t,n,k;
    scanf("%lld",&t);
    for(lli z=1;z<=t;++z)
    {
        std::priority_queue<pair<lli,lli>, vector<pair<lli,lli> >, ComparisonClass>pq;
        printf("Case #%lld: ",z);
        scanf("%lld%lld",&n,&k);
        pq.push(mp(n,1));
        lli x=0,y=0,l=0,last=0;
        pair<lli,lli> p,s;
        while(!pq.empty() && x<k)
        {
            p=pq.top();
            //cout<<p.first<<" "<<p.second<<" "<<x<<endl;
            pq.pop();
            s=mp(-1,-1);
            if(!pq.empty())
            {
                s=pq.top();
            }
            if(p.first==s.first)
            {
                pq.pop();
                p.second+=s.second;
                pq.push(p);
            }
            else
            {
                last=p.first;
                y=p.first;
                l=p.second;
                //if(y>=1)
                //cout<<y<<endl;
                pq.push(mp(y/2,l));
                //if(y>=1)
                pq.push(mp((y-1)/2,l));
                x+=l;
            }
        }
        printf("%lld %lld\n",last/2,(last-1)/2);
    }
}
