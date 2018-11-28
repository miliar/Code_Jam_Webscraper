#include <bits/stdc++.h>

using namespace std;

typedef long long li;

#define all(v) (v).begin(), (v).end()

// segments
// choose max length leftest, split by 2

bool tidy(li x)
{
    vector<int> d;
    while (x)
    {
        d.push_back(x % 10);
        x /= 10;
    }
    reverse(all(d));
    for (int i = 0; i + 1 < (int)d.size(); i++)
        if (d[i] > d[i + 1])
            return false;
        
    return true;
}

li solve(li n)
{
    for (li x = n; x >= 1; x--)
        if (tidy(x))
            return x;
        
    return -1;
}

int main()
{
    int nt;
    cin >> nt;
    
    for (int i = 0; i < nt; i++)
    {
        li n;
        cin >> n;
        auto p = solve(n);
        cout << "Case #" << i + 1 << ": " << p << '\n';
    }
    
    return 0;
}
