#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
bool seat[1000005];
struct Place
{
    int l,r;
    Place(int _l=0,int _r=0):l(_l),r(_r){}
    bool operator<(const struct Place&x)const
    {
        int id=l+r>>1;
        int id2=x.l+x.r>>1;
        int l1=id-l-1;
        int r1=r-id-1;
        int l2=id2-x.l-1;
        int r2=x.r-id2-1;
        if(min(l1,r1)!=min(l2,r2))
            return min(l1,r1)<min(l2,r2);
        else if(max(l1,r1)!=max(l2,r2))
            return max(l1,r1)<max(l2,r2);
        else return id>id2;
    }
};
int main()
{
    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("c1.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        priority_queue<Place>pq;
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i=1; i<=n; ++i)
            seat[i]=0;
        seat[0]=seat[n+1]=1;
        pq.push(Place(0,n+1));
        pair<int,int>ans;
        for(int i=0; i<k; ++i)
        {
            Place temp=pq.top();
            pq.pop();
            int id=temp.l+temp.r>>1;
            if(id>temp.l+1)
            {
                pq.push(Place(temp.l,id));
            }
            if(temp.r>id+1)
            {
                pq.push(Place(id,temp.r));
            }
            ans=make_pair(min(id-temp.l-1,temp.r-id-1),max(id-temp.l-1,temp.r-id-1));
        }
        printf("Case #%d: %d %d\n",++ca,ans.second,ans.first);
        fprintf(stderr,"Case #%d: %d %d\n",ca,ans.second,ans.first);
    }
}
