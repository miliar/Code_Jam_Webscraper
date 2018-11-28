#include <bits/stdc++.h>
using namespace std;
using namespace std::chrono;
#define DBG(x) cout << #x << " = " << x << endl;
/*
Compile:
    -Wall -Wextra -pedantic -std=c++14 -O2 -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wcast-qual -Wcast-align -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC -D_FORTIFY_SOURCE=2 -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -fstack-protector 

    -std=c++14 -O2
 
Check for memory usage:
    valgrind --tool=massif
*/


pair<int, int> solve()
{
    int n, k;
    cin >> n >> k;

    priority_queue<pair<int, int>> q;
    q.push(make_pair(n, -1));

    for (int i = 1; i <= n; i++) 
    {
        auto stall = q.top();
        q.pop();

        int sz = stall.first;
        int start = -stall.second;

        int split_place = start + sz / 2 - !(sz & 1);

        int end = start + sz - 1;

        if (split_place != start)
        {
            q.push(make_pair(split_place - start, -start));
        }
        if (split_place != end)
        {
            q.push(make_pair(end - split_place, -(split_place + 1)));
        }
        
        if (i == k)
        {
            return make_pair(sz / 2, sz / 2 - !(sz & 1));
        }
    }

    return {0, 0};
}


int main()
{   
    cin.sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        auto x = solve();
        cout << "Case #" << i << ": " << x.first << " " << x.second << endl;
    }
    return 0;
}
