#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int next(int last, vector<char>& out)
{
    int N = out.size();
    int x = last + 2;
    while(true)
    {
        x %= N;
        if (out[x] == 0)
            return x;

        x++;
    }

    return -1;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        int mx = max(R, max(Y, B));
        int mn = min(R, min(Y, B));
        int mm = N - mx - mn;

        if (mx > (mn + mm))
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        else
        {
            cout << "Case #" << t << ": ";
            vector<pair<int, char> > v;
            v.push_back(make_pair(R, 'R'));
            v.push_back(make_pair(Y, 'Y'));
            v.push_back(make_pair(B, 'B'));

            sort(v.begin(), v.end());

            vector<char> out(N, 0);
            int last = 0;
            out[0] = v.back().second;
            --(v.back().first);
            for (int i = 2; i >= 0; --i)
            {
                for (int j = 0; j < v[i].first; ++j)
                {
                    last = next(last, out);
                    out[last] = v[i].second;
                }
            }

            string ans = "";
            for (int i = 0; i < out.size(); ++i)
                ans.push_back(out[i]);

            cout << ans << endl;
        }
    }
}
