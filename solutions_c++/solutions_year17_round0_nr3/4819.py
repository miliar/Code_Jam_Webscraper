#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    int n,k;
    int i;
    for(i=0;i<t;i++)
    {
        priority_queue <pair<int, pair<int,int> > > heap;
        scanf("%d%d",&n,&k);
        heap.push(make_pair(n,make_pair(1,n)));
        int j;
        pair<int,pair<int,int> > temp;
        int t1,t2;
        for(j=0;j<k;j++)
        {
            temp=heap.top();
            heap.pop();
            int l=temp.second.first;
            int r=temp.second.second;
            int mid=(l+r)/2;
            if(j==k-1)
            {
                t1=mid-l;
                t2=r-mid;
            }
            heap.push(make_pair(mid-l,make_pair(l,mid-1)));
            heap.push(make_pair(r-mid,make_pair(mid+1,r)));
        }
        printf("Case #%d: %d %d\n",i+1,max(t1,t2),min(t1,t2));
    }
    return 0;
}
