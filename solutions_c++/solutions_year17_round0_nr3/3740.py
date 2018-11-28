#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct node
{
    int l,r,len;
    node(int a=0,int b=0)
    {
        l=a,r=b;
        len=r-l-1;
    }
    bool operator <(const node &b)const
    {
        return len<b.len;
    }

};

priority_queue<node>q;
int main()
{
    int n,k;
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("outputc2.txt","w",stdout);
    int t;
    int cnt=1;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        while(!q.empty())q.pop();
        q.push(node(0,n+1));
        int ans=-1;
        printf("Case #%d: ",cnt++);
        while(k--)
        {

            node t=q.top();
            int ll=t.l,rr=t.r;
            int idx=(ll+rr)/2;
            if (k==0)
            {
                int ls=(idx-ll-1);
                int rs=(rr-idx-1);
                printf("%d %d\n",max(ls,rs),min(ls,rs));
            }
            q.push(node(ll,idx));
            q.push(node(idx,rr));
            q.pop();
        }


    }



    return 0;
}
//896521 183995
