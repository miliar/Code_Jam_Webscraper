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
        int n=sz(s);

        int prob=-1;
        int g=n;
        while(g--)
        for(int i=0;i<n-1;i++)
        {
            if(s[i]>s[i+1])
            {
                prob=i;
                s[prob]=char(s[prob]-1);
                for(int j=prob+1;j<n;j++)
                    s[j]='9';
                break;
            }
        }
        int index=0;
        while(s[index]=='0')
            index++;
        cout<<"Case #"<<test<<": ";
        for(int i=index;i<n;i++)
            cout<<s[i];

        cout<<endl;
    }


    return 0;
}


