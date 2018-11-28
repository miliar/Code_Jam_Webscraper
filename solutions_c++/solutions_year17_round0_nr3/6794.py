#include <bits/stdc++.h>

using namespace std;

typedef long long li;

// segments
// choose max length leftest, split by 2

pair<li, li> solve(li n, li k)
{
    set<pair<li, li>> segs;
    segs.emplace(-n, 0);
    
    for (int t = 0; t < k; t++)
    {
        auto s = *segs.begin();
        int x = s.second;
        int l = -s.first;
        segs.erase(segs.begin());
        
        //printf("%d %d\n", x, l);
        
        if ((l - 1) / 2 > 0)
            segs.emplace(-((l - 1) / 2), x);
        
        if (l - 1 - (l - 1) / 2 > 0)
            segs.emplace(-(l - 1 - (l - 1) / 2), x + (l - 1) / 2 + 1);
        
        if (t + 1 == k)
            return make_pair(l - 1 - (l - 1) / 2, (l - 1) / 2);
    }
    
    assert(!"imp");
}

int main()
{
    int nt;
    cin >> nt;
    
    for (int i = 0; i < nt; i++)
    {
        li n, k;
        cin >> n >> k;
        auto p = solve(n, k);
        cout << "Case #" << i + 1 << ": " << p.first << " " << p.second << '\n';
    }
    
    return 0;
}
