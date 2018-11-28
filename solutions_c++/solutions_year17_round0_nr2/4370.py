#include<bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define lol long long
#define fc cin.tie(NULL);ios_base::sync_with_stdio(false);

using namespace std;

const double pi = M_PI;
const double E = M_E;
const int N = 1e3+5;
const int M = 1e3;
const int inf = 1e9;
const int md = 1e9+7;

int t,n,i,j,e;
string s, ans;

int main()
{
    fc

    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int it = 0;
    cin>>t;
    while (t--)
    {
        cin>>s;

        n = s.size();
        ans = s[0];
        for (i=1; i<n; ++i)
        {
            if (s[i] >= s[i-1])
            {
                ans += s[i];
                continue;
            } else
            {
                j = i-1;
                while (j > 0 && ans[j] == ans[j-1])
                 --j;
                if (j == 0 && ans[j] == '1')
                {
                    ans = "";
                    for (j=0; j<n-1; ++j)
                     ans += '9';
                    break;
                } else
                {
                    ans = s.substr(0, j+1);
                    --ans[ans.size()-1];
                    for (e = j+1; e<n; ++e)
                     ans += '9';
                    break;
                }
            }
        }

        ++it;
        cout<<"Case #"<<it<<": ";
        cout<<ans<<"\n";
    }
}
