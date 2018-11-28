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
        string s;
        cin>>s;
        int k;
        cin>>k;
        int n=sz(s);
        int counat=0;
        for(int i=0;i+k<=n;i++)
        {
            if(s[i]=='-')
            {
                //cout<<i<<" ";
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
                counat++;
            }
        }
        bool flag=0;
        for(int i=0;i<n;i++)
            if(s[i]=='-')
                flag=1;
        if(flag)
            cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<test<<": "<<counat<<endl;
    }
    return 0;
}


