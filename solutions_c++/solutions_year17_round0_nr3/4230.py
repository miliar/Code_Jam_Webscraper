#include<bits/stdc++.h>
using namespace std;
#define pii pair<long long int,long long int>
#define fi first
#define se second
#define lli long long int
struct mycom
{
    bool operator()(pair<int,int> p,pair<int,int> q)
    {
       return (p.second - p.first ) < (q.second - q.first);
    }
};
int main()
{   freopen("sub-5.in","r",stdin);
    freopen("inp.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        long long int n,k;
        cin>>n>>k;
        priority_queue< pii, vector<pii >, mycom > myqu;
        myqu.push(make_pair(1,n+2));
        pii p;
        lli mid;
        for(int i=0;i<k;i++)
        {
            p=myqu.top();
            //cout<<p.fi<<" "<<p.se<<"\n";
            myqu.pop();
            mid=p.fi+(p.se-p.fi)/2;
            myqu.push(make_pair(p.fi,mid));
            myqu.push(make_pair(mid,p.se));

        }
        cout<<"Case #"<<test<<": ";
        cout<<max(p.se-mid-1,mid-p.fi-1)<<" "<<min(p.se-mid-1,mid-p.fi-1)<<"\n";
    }
return 0;
}
