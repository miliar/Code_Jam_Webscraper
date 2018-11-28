#include<iostream>
#include<algorithm>
#include<math.h>
#include<cstring>
#include<iomanip>
#include<stdio.h>
#include<limits>
#include<unordered_map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#define gcd __gcd
#define pb(x) push_back(x)
#define ll long long
#define in(x) scanf("%d",&x)
#define mod 1000000007LL
#define sz(x) x.size()
#define mst(x,a) memset(x,a,sizeof(x))
#define pii pair<ll,ll>
#define F first
#define S second
#define m_p make_pair
#define all(v) (v.begin(),v.end())
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        int n,k;
        cin>>n>>k;
        vector<int>v;
        v.pb(n);
        while(k--)
        {
            int maxi=0;
            for(int i=1;i<sz(v);i++)
            {
                if(v[maxi]<v[i])
                    maxi=i;
            }
            int now=v[maxi]-1;
            vector<int>temp;
            for(int i=0;i<maxi;i++)
                temp.pb(v[i]);
            temp.pb(now/2);
            temp.pb(now-now/2);
            for(int i=maxi+1;i<sz(v);i++)
                temp.pb(v[i]);
            v.clear();
            for(int i=0;i<sz(temp);i++)
                v.pb(temp[i]);
            int ans1=max(now/2,now-now/2);
            int ans2=min(now/2,now-now/2);
            if(k==0)
                cout<<"Case #"<<test<<": "<<ans1<<" "<<ans2<<endl;
//            for(int i=0;i<sz(v);i++)
//                cout<<v[i]<<" ";
//            cout<<endl;
        }
    }
    return 0;
}


