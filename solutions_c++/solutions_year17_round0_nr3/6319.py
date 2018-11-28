#include <bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
using namespace std;

const int N = 3000020;
priority_queue<pair<int, int> > q;
///len l

int main()
{
    //freopen("C-small-2-attempt0.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for(int qq = 0; qq < t; ++qq)
    {
        int k, n;
        cin >> n >> k;
        q.push(mp(n, -1));
        for(int i = 0; i < k; ++i)
        {
            pair<int, int > top = q.top();
            int pos = (top.f + 1) / 2;
            q.pop();
            if(n > 1)
            {
                q.push(mp(top.f - pos, top.s - pos));
                if(n > 2)
                    q.push(mp(pos - 1, top.s));
            }
            if(i == k - 1)
            {
                top.s = top.f - pos;
                top.f = pos - 1;
                cout << "Case #" << qq+1 << ": ";
                cout << max(top.f, top.s) << ' ' << min(top.f, top.s) << '\n';
            }
        }
        while(q.size() > 0)
            q.pop();
    }
}
