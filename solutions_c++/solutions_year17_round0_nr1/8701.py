#include <bits/stdc++.h>

using namespace std;

typedef long long li;

#define all(v) (v).begin(), (v).end()

string solve(string s, int k)
{
    int n = s.length();
    
    vector<vector<int>> e(1 << n);
    
    for (unsigned m = 0; m < (1 << n); m++)
        for (int i = 0; i + k - 1 < n; i++)
        {
            unsigned left = m & ((1 << i) - 1);
            unsigned right = (m >> (i + k)) << (i + k);
            unsigned middle = (((~m) >> i) & ((1 << k) - 1)) << i;
            unsigned to = left | middle | right;
            //printf("to %d\n", to);
            e[m].push_back(to);
            
            //printf("%d %d %d\n", left, middle, right);
            
            //for (int i = 0; i < n; i++) printf("%c", m & (1 << i) ? '+' : '-');
            //printf(" -> ");
            //for (int i = 0; i < n; i++) printf("%c", to & (1 << i) ? '+' : '-');
            //printf("\n");
        }
        
    int start = 0;
    for (int i = 0; i < n; i++)
        if (s[i] == '-')
            start |= 1 << i;
        
    deque<int> q;
    vector<int> d(1 << n, -1);
    q.push_back(start);
    d[start] = 0;
    
    while (!q.empty())
    {
        int v = q.front();
        q.pop_front();
        
        for (int u: e[v])
        {
            if (d[u] == -1)
            {
                d[u] = d[v] + 1;
                q.push_back(u);
            }
        }
    }
    
    return d[0] == -1 ? "IMPOSSIBLE" : to_string(d[0]);
}

int main()
{
    int nt;
    cin >> nt;
    
    for (int i = 0; i < nt; i++)
    {
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << i + 1 << ": " << solve(s, k) << '\n';
    }
    
    return 0;
}
