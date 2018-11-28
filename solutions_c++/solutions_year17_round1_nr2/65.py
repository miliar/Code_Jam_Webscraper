#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T;

    cin >> T;
    for (int ct = 0; ct < T; ++ct)
    {
        int n, p;
        vector<int> r;

        cin >> n >> p;
        for (int i = 0; i < n; ++i)
        {
            int _;
            cin >> _;
            r.push_back(_);
        }

        vector<vector<pair<int,int>>> choices;
        vector<int> pts;
        for (int i = 0; i < n; ++i)
        {
            vector<pair<int,int>> i_choices;
            for (int j = 0; j < p; ++j)
            {
                int _;
                cin >> _;

                int lb = (_ * 10 + 11 * r[i] - 1) / (11 * r[i]);
                int ub = _ * 10 / 9 / r[i];
                if (lb <= ub)
                {
                    i_choices.push_back(make_pair(ub, lb));
                    pts.push_back(lb);
                    pts.push_back(ub);
                }
            }
            sort(i_choices.begin(), i_choices.end());
            choices.push_back(i_choices);
        }

        sort(pts.begin(), pts.end());
        pts.erase(unique(pts.begin(), pts.end()), pts.end());

        int ans = 0;
        for (int pt : pts)
        {
            while (true)
            {
                bool ok = true;
                for (int i = 0; i < n; ++i)
                {
                    bool i_ok = false;
                    for (size_t j = 0; j < choices[i].size(); ++j)
                    {
                        if (choices[i][j].second <= pt && choices[i][j].first >= pt)
                        {
                            i_ok = true;
                            break;
                        }
                    }
                    if (!i_ok)
                    {
                        ok = false;
                        break;
                    }
                }

                if (!ok)
                {
                    break;
                }

                ++ans;
                for (int i = 0; i < n; ++i)
                {
                    for (auto j = choices[i].begin(); j != choices[i].end(); ++j)
                    {
                        if (j->second <= pt && j->first >= pt)
                        {
                            choices[i].erase(j);
                            break;
                        }
                    }
                }
            }
        }

        cout << "Case #" << (ct + 1) << ": " << ans << endl;
    }
    return 0;
}
