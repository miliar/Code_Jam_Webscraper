#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("b.in");
    ofstream cout("output.txt");
    int T;
    cin >> T;
    for (int Tk = 0; Tk < T; ++Tk)
    {
        int ac, aj;
        cin >> ac >> aj;
        vector <int> Sc(ac), Fc(ac), Sj(aj), Fj(aj);
        vector <pair <int, pair <int, int> > > L;
        vector <int> l(2);
        for (int i = 0; i < ac; ++i)
        {
            cin >> Sc[i] >> Fc[i];
            L.push_back({Sc[i], {0, Fc[i]}});
            l[0] += Fc[i] - Sc[i];
        }
        for (int i = 0; i < aj; ++i)
        {
            cin >> Sj[i] >> Fj[i];
            L.push_back({Sj[i], {1, Fj[i]}});
            l[1] += Fj[i] - Sj[i];
        }
        sort(L.begin(), L.end());
        vector <vector <int> > D(2);
        int cur = 0;
        L.push_back({L[0].first + 24 * 60, {L[0].second.first, L[0].second.second + 24 * 60}});
        for (int i = 0; i + 1 < L.size(); ++i)
        {
            if (L[i].second.first == L[i + 1].second.first)
            {
                D[L[i].second.first].push_back(L[i + 1].first - L[i].second.second);
                ++cur;
            }
            ++cur;
        }
        for (int i = 0; i < 2; ++i)
        {
            sort(D[i].begin(), D[i].end());
            int j = 0;
            while (j < D[i].size() && l[i] <= 720)
            {
                l[i] += D[i][j];
                ++j;
            }
            if (l[i] > 720)
            {
                --j;
            }
            cur -= 2 * j;
        }
        cout << "Case #" << Tk + 1 << ": ";
        cout << cur << endl;
    }
    return 0;
}
