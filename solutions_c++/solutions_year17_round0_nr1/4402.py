#include<bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define lol long long
#define fc cin.tie(NULL);ios_base::sync_with_stdio(false);

using namespace std;

const double pi = M_PI;
const double e = M_E;
const int N = 1e3+5;
const int M = 1e3;
const int inf = 1e9;
const int md = 1e9+7;

int t,n,k,i,add,ans,cur;
bool can;
int a[N];
string s;

int main()
{
    fc

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int it = 0;
    cin>>t;
    while (t--)
    {
        cin>>s;
        cin>>k;

        memset(a, 0, sizeof(a));
        n = s.size();
        add = 0;
        ans = 0;
        for (i=0; i<n-k+1; ++i)
        {
            add += a[i];

            cur = ((s[i] == '-' ? 1 : 0) + add % 2) % 2;
            if (cur)
            {
                ++ans;
                ++add;
                --a[i+k];
            }
        }
        can = true;
        for (i=n-k+1; i<n; ++i)
        {
            add += a[i];

            cur = ((s[i] == '-' ? 1 : 0) + add % 2) % 2;
            if (cur) can = false;
        }

        ++it;
        cout<<"Case #"<<it<<": ";

        if (can) cout<<ans<<"\n";
        else cout<<"IMPOSSIBLE\n";
    }
}
