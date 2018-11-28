#include <iostream>
#include <vector>
#include <cstdio>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <string.h>

#define ll long long int
#define li long int
#define pi pair<int,int>
#define pl pair<li,li>
#define pll pair<ll,ll>
#define mem0(a) memset(a,0,sizeof(a))
#define mem1(a) memset(a,-1,sizeof(a))
#define MOD 1000000007
#define loop(i,n) for(ll i=0;i<n;i++)
#define loop1(i,n) for(ll i=1;i<=n;i++)
#define fast_input cin.tie(0);ios_base::sync_with_stdio(0);

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int p=0;
    while(t--)
    {
        p++;
        string s;
        cin>>s;
        int n=s.size();
        int k;
        cin>>k;
        int count=0;
        for(int i=0;i<=n-k;i++)
        {
            if(s[i]=='-')
            {
                count++;
                for(int j=i;j<k+i;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else if(s[j]=='+')
                        s[j]='-';
                }
            }
        }
        bool ans=true;
        for(int i=n-1;i>n-k;i--)
        {
            if(s[i]=='-')

                {
                    ans=false;
                    break;
                }
        }
        cout<<"Case #"<<p<<": ";
        if(ans==false)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<count<<endl;
    }
    return 0;
}
