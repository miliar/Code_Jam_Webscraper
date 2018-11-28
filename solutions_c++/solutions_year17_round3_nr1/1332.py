#include<bits/stdc++.h>
#define pb2 push
#define pb push_back
#define mp make_pair
#define ll long long
#define fi first
#define se second
#define ld long double
using namespace std;
struct node{
ld h,r,csa;
} a[1004];
ld pi=3.1415926535897932384626;
bool check(node a,node b)
{
    return a.r<b.r;
}
int main()
{
    freopen("txtin.txt","r",stdin);
    freopen("txtout.txt","w",stdout);
    ll t,n,i,j,k,l;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        cout<<"Case #"<<test<<": ";
        cin>>n>>k;
        for(i=0;i<n;i++)
        {

            cin>>a[i].r>>a[i].h;
            a[i].csa=pi*2.0*a[i].h*a[i].r;
        }
        sort(a,a+n,check);
        ld ans=0.0,ans2=0.0;
        priority_queue<ld,vector<ld>,greater<ld> > pq;
        for(i=n-1;i>=0;i--)
        {
            ans=a[i].csa+(pi*a[i].r*a[i].r);
            ans2=max(ans,ans2);
            for(j=i-1;j>=max(i-k+1,(ll)0);j--)
            {
                pq.push(a[j].csa);
            }
            if(pq.empty())
                continue;
            for(j=i-k;j>=0;j--)
            {
                pq.push(a[j].csa);
                pq.pop();

            }
            //cout<<pq.size()<<" ";
            while(!pq.empty())
            {
                ans+=pq.top();
                pq.pop();
            }
            ans2=max(ans2,ans);
        }
        printf("%.10Lf\n",ans2);
    }
    return 0;
}
