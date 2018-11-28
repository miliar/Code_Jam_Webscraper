#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;

#define LSOne(S) (S & (-S))
#define MOD 1000000009
#define INF 1000000000

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef pair<string, int> ps;
typedef pair<int, char> pc;
typedef pair<pi, int> pii;
typedef pair<double, double> pd;
typedef pair<ll, ll> pll;

typedef
tree<
  int,
  null_type,
  less<int>,
  rb_tree_tag,
  tree_order_statistics_node_update>
ordered_set;


int main()
{
    std::ios::sync_with_stdio(false);
    ifstream is("A-large.in");
    ofstream os("A-large.out");
    int tc;
    //cin >> tc;
    is >> tc;

    for(int i = 0; i < tc; ++i)
    {
        string str; int k;
        //cin >> str >> k;
        is >> str >> k;
        bool can = true;
        int ans = 0;

        for(int j = 0; j < str.size(); ++j)
        {
            if(str[j] == '-' && (j + k - 1) < str.size())
            {
                ++ans;
                for(int z = j; z <= (j+k-1); ++z)
                {
                    (str[z] == '-') ? str[z] = '+' : str[z] = '-';
                }
            }
        }

        for(auto ch : str)
        {
            if(ch == '-')
            {
                can = false;
            }
        }

        //cout << "Case #" << (i+1) << ": ";
        os << "Case #" << (i+1) << ": ";
        //(can) ? cout << ans << "\n" : cout << "IMPOSSIBLE\n";
        (can) ? os << ans << "\n" : os << "IMPOSSIBLE\n";
    }
    return 0;
}

