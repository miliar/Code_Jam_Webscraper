#include <bits/stdc++.h>

#define all(x) x.begin(), x.end()

using namespace std;

int n;
map <string, bool> was;
map <string, int> dist;

queue <string> q;

int main()
{
   freopen("A-small-attempt0.in", "r", stdin);
   freopen("A-small-attempt0.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    //cout << fixed << setprecision(20);

    int t;
    cin >> t;

    for (int p = 0; p < t; p++)
    {
        string s;
        int k;
        was.clear();
        dist.clear();

        cin >> s >> k;

        q.push(s);
        dist[s] = 1;
        was[s] = 1;
        while (!q.empty())
        {
            string v = q.front();
            q.pop();

            for (int i = 0; i <= v.size() - k; i++)
            {
                string now = v;

                for (int j = i; j < i + k; j++)
                {
                    if (now[j] == '+') now[j] = '-';
                    else now[j] = '+';
                }

                if (!was[now])
                {
                    was[now] = 1;
                    dist[now] = dist[v] + 1;
                    q.push(now);
                }
            }
        }

        for (int i = 0; i < s.size(); i++)
            s[i] = '+';

        cout << "Case #" << p + 1 <<  ": ";
        if (dist[s] == 0)
            cout << "IMPOSSIBLE\n";
        else
            cout << dist[s] - 1 << endl;

    }


    return 0;
}
