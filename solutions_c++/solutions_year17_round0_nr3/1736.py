#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define ll long long
map<ll,ll>my;
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        ll n,k,ct=0;
        cin>>n>>k;
        my.clear();
        my[n]=1;
        printf("Case #%d: ",cs);
        while(1)
        {
            map<ll,ll>::reverse_iterator it=my.rbegin();
            ll p=it->f;
            ll c=it->s;
            my.erase(p);
            ct+=c;
            if(ct>=k)
            {
                cout<<p/2<<" "<<(p-1)/2<<endl;
                break;
            }
            my[(p-1)/2]+=c;
            my[p/2]+=c;
        }
        my.clear();
        cs++;
    }
    return 0;
}
