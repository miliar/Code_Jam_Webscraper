#include <bits/stdc++.h>

#define mod 1000000007
#define inf 1000000000000LL
#define root2 1.41421
#define root3 1.73205
#define pi 3.14159
#define MAX 100001
#define cntbit __builtin_popcountll
#define ll long long int
#define PII pair<int, int>
#define f first
#define s second
#define mk make_pair
#define PLL pair<ll, ll>
#define gc getchar
#define pb push_back

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, k, n, i, ca=1, ans, j;
    string s;
    string imp="IMPOSSIBLE";
    cin>>t;
    while(ca<=t)
    {
        cout<<"Case #"<<ca<<": ";
        cin>>s>>k;
        n=s.size();
        ans=0;
        for(i=0;i<=n-k;i++)
        {
            if(s[i]=='+')continue;
            ans++;
            for(j=i;j<i+k;j++)
            {
                if(s[j]=='-')s[j]='+';
                else s[j]='-';
            }
        }
        for(i=n-k;i<n;i++)
            if(s[i]!='+')break;
        if(i==n)
            cout<<ans<<endl;
        else
            cout<<imp<<endl;
        ca++;
    }
}
