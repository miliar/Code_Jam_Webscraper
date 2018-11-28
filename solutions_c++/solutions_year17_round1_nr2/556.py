#include <string>
#include <fstream>
//#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <set>
#include <string>
#include <list>
using namespace std;

pair<int,int> a(int x, int s)
{
    int q = (x * 10 -1) / 11 + 1;
    int w = x * 10 / 9;
    return make_pair((q-1) / s + 1, w/s);
}


int main()
{
    ifstream in("B-large.in");
    ofstream out("out.txt");
    int n;
    in >> n;
    for (int i = 0; i < n; ++i)
    {
        int N, P;
        in >> N >> P;

        vector<int> R(N);
        for (int i = 0; i < N; ++i) in >> R[i];

        vector<list<int>> Q(N);
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < P; ++j)
            {
                int c;
                in >> c;
                Q[i].push_back(c);
            }

        for (int i = 0; i < N; ++i)
            Q[i].sort();

        int result = 0;

        while (true) // todo
        {
            vector<pair<int, int>> Z(N);
            bool finish = false;
            for (int i = 0; i < N; ++i)
            {
                if (Q[i].begin() == Q[i].end())
                {
                    finish = true;
                    break;
                }
                Z[i] = a(Q[i].front(), R[i]);
            }
            if (finish) break;

            int mx = -1;
            for (int i = 0; i < N; ++i)
            {
                mx = max(mx, Z[i].first);
            }

            bool ok = true;

            for (int i = 0; i < N; ++i)
            {
                if (Z[i].second < mx || Z[i].second < Z[i].first)
                {
                    ok = false;
                    Q[i].erase(Q[i].begin());
                }
            }

            if (ok)
            {
                for (int i = 0; i < N; ++i)
                {
                    Q[i].erase(Q[i].begin());
                }
                ++result;
            }
        }

        out << "Case #" << (i + 1) << ": " << result << endl;
    }

    return 0;
}

