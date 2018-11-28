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

bool isSorted(string str)
{
    string cpy = str;
    sort(cpy.begin(), cpy.end());
    return (str == cpy);
}


int main()
{
    std::ios::sync_with_stdio(false);
    ifstream is("B-large.in");
    ofstream os("B-large.out");
    int tc;
    //cin >> tc;
    is >> tc;

    for(int i = 0; i < tc; ++i)
    {
        string str;
        //cin >> str;
        is >> str;

        while(!isSorted(str))
        {
            for(int i = 0; i < str.size()-1; ++i)
            {
                if(str[i] > str[i+1])
                {
                    for(int j = i+1; j < str.size(); ++j)
                    {
                        str[j] = '9';
                    }

                    if(str[i] == '0') str[i] = '9';
                    else --str[i];

                    if(i == 0 && str[i] == '0')
                    {
                        int sz = str.size();
                        str = "";
                        for(int j = 1; j < sz; ++j)
                        {
                            str += '9';
                        }
                    }
                }
            }
        }

        //cout << "Case #" << (i+1) << ": " << str << "\n";
        os << "Case #" << (i+1) << ": " << str << "\n";
    }
    return 0;
}

