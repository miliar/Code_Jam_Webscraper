#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

typedef long long ll;
#define S(a) scanf("%d",&a)
#define LS(a) scanf("%lld",&a)
#define FOR(i,a,b) for(int i = a, i <= b; ++i)
#define DOW(i,b,a) for(int i = b; i >= a; --i)
const ll INF = 1e17;
const ll MOD = 1e9 + 7;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    S(t);
    for(int tc = 1; tc <= t; ++tc)
    {
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        int ans = 0;
    //    cout << s << " \n";

        for(int i = 0; i <= n - k; ++i)
        {

            if(s[i] == '-')
            {

                ans++;
                for(int j = 0; j <  k; j++)
                {

                    if(s[j + i] == '-')
                    {
                        s[j + i] = '+';
                    }
                    else s[j + i] = '-';

                }


            }


        }
 // cout << s << "\n";

        cout << "Case #" << tc << ": ";
        for(int p = 0 ; p < n ; ++p)
        {
            if(s[p] == '-')
            {
                cout << "IMPOSSIBLE\n";
                ans = -1;
                break;
            }
        }
        if(ans != -1)
        cout << ans << "\n";


    }
     return 0;
  }

