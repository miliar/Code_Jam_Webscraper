#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
typedef long long ull;
using namespace std;
typedef pair<ull, ull> ppi; 

ppi divide(ull n)
{
    if (n % 2 == 0)
        return make_pair(n / 2, (n - 1) / 2);
    else
        return make_pair(n / 2, n / 2);
}

ppi solve(ull n, ull k)
{
    map<ull, ull> cnt;
    cnt[-n] = 1;
    while(true)
    {
        ppi cur = *cnt.begin();
        cur.first *= -1;
        cnt.erase(cnt.begin());
        if (k <= cur.second)
            return divide(cur.first);
        else
        {
            ppi ne = divide(cur.first);
            cnt[-ne.first] += cur.second;
            cnt[-ne.second] += cur.second;
            k -= cur.second;
        }
    }
    return make_pair(0, 0);
}

int main()
{
    ull n, k, t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> n >> k;
        ppi ans = solve(n, k);
        cout <<  "Case #" << i + 1 << ": " << ans.first << " " << ans.second << endl;
    }
}
