#include<bits/stdc++.h>
using namespace std;

int n,c,m,t[2000],a[2000];

int f(int k)
{
    int ret=0;
    for(int i=1;i<=n;i++)
        ret+=max(0,a[i]-k);
    return ret;
}

bool check(int k)
{
    int sum=0;
    for(int i=1;i<=n;i++)
    {
        sum+=k;
        if(a[i]>sum) return false;
        sum-=a[i];
    }
    return true;
}

int main()
{
    ifstream cin("in");
    ofstream cout("out");
    int qw;
    cin>>qw;
    for(int q=1;q<=qw;q++)
    {
        cin>>n>>c>>m;
        memset(a,0,sizeof a);
        memset(t,0,sizeof t);
        int l=0,r=m;
        for(int i=0;i<m;i++)
        {
            int p,b;
            cin>>p>>b;
            t[b]++;
            l=max(l,t[b]);
            a[p]++;
        }
        while(l<r)
        {
            int mid=(l+r)/2;
            if(check(mid))
                r=mid;
            else
                l=mid+1;
        }
        cout<<"Case #"<<q<<": "<<l<<" "<<f(l)<<endl;
    }
}
