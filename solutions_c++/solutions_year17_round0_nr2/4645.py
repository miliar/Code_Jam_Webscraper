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
        bool ans=true;
        bool one=false;
        int j=-1;
        if(s[0]=='1')
            one=true;
        for(int i=0;i<s.size()-1;i++)
        {
            if(one==true&&s[i]=='1'&&s[i+1]=='0')
            {
                ans=false;
                j=-2;
                break;
            }
            if(s[i]>s[i+1])
            {
                ans = false;
                j=i;
                break;
            }
        }
        cout<<"Case #"<<p<<": ";
        if(ans==true)
         cout<<s<<endl;
        else if(j==-2)
        {
            for(int i=0;i<s.size()-1;i++)
                cout<<'9';
            cout<<endl;
        }
        else
        {
            while(j!=0&&s[j]==s[j-1])
                j--;
            for(int i=0;i<j;i++)
                cout<<s[i];
            cout<<(char)(s[j]-1);
            for(int i=j+1;i<s.size();i++)
                cout<<'9';
            cout<<endl;
        }

    }
    return 0;
}
