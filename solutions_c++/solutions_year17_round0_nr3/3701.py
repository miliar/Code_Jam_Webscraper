#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

struct cmp
{
    bool operator() (const pair <int, int> &a, const pair <int, int> &b) const
    {
        if (a.second - a.first != b.second - b.first)
            return a.second - a.first > b.second - b.first;
        return a.first < b.first;
    }
};

set <pair <int, int>, cmp> s;

#undef int
int main()
{
#define int long long
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        int n, k; cin >> n >> k;
        s.clear();
        s.insert(make_pair(1, n));
        int ans1, ans2;
        while (true)
        {
            pair <int, int> p = *s.begin();
            s.erase(s.begin());
            int mid = (p.first + p.second) / 2;
            if (k == 1)
            {
                ans1 = mid - p.first;
                ans2 = p.second - mid;
                break;
            }
            s.insert(make_pair(p.first, mid - 1));
            s.insert(make_pair(mid + 1, p.second));
            k--;
        }
        if (ans1 < ans2)
            swap(ans1, ans2);
        cout << "Case #" << tt << ": " << ans1 << " " << ans2 << "\n";
    }
    return 0;
}
