#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>

using namespace std;

void GetLR(long long x, long long &L, long long &R)
{
    if (x % 2 == 1)
    {
        L = x / 2;
        R = x / 2;
    }
    else
    {
        L = x / 2 - 1;
        R = x / 2;
    }
}


int main()
{
    int nr_tests;
    ifstream f("input.txt");
    ofstream g("output.txt");

    f >> nr_tests;
    for (int test = 1; test <= nr_tests; ++ test)
    {
        long long N, K;
        f >> N >> K;
        map<long long, long long> m[2];

        int p = 0, q = 1;
        m[0][N] = 1;
        bool gata = false;
        while (!gata)
        {
            for (map<long long, long long> :: reverse_iterator it = m[p].rbegin(); it != m[p].rend(); ++ it)
            {
                long long lg = it->first;
                long long cnt = it->second;

                if (cnt < K)
                {
                    K -= cnt;
                    long long L, R;
                    GetLR(lg, L, R);
                    if (m[q].find(L) != m[q].end())
                    {
                        m[q][L] = m[q][L] + cnt;
                    }
                    else
                    {
                        m[q][L] = cnt;
                    }

                    if (m[q].find(R) != m[q].end())
                    {
                        m[q][R] = m[q][R] + cnt;
                    }
                    else
                    {
                        m[q][R] = cnt;
                    }
                }
                else
                {
                    long long L, R;
                    GetLR(lg, L, R);
                    g << "Case #" << test << ": " << max(L, R) << " " << min(L, R) << "\n";
                    gata = true;
                    break;
                }
            }
            if (!gata)
            {
                m[p].clear();
                swap(p, q);
            }
            else
            {
                m[p].clear();
                m[q].clear();
            }
        }
    }

    f.close();
    g.close();

    return 0;
}
