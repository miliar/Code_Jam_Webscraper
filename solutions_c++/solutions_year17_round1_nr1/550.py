#include <string>
#include <fstream>
//#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <set>
#include <string>
using namespace std;
int main()
{
    ifstream in("A-large.in");
    ofstream out("out.txt");
    int n;
    in >> n;
    for (int i = 0; i < n; ++i)
    {
        int R, C;
        in >> R >> C;

        vector<string> M(R);
        for (int i = 0; i < R; ++i)
        {
            in >> M[i];
        }

        vector<int> G(R, false);

        for (int i = 0; i < R; ++i)
        {
            char c = '\0';
            for (int j = 0; j < C; ++j)
            {
                if (M[i][j] == '?')
                {
                    if (c)
                    {
                        M[i][j] = c;
                    }
                }
                else
                {
                    c = M[i][j];
                    G[i] = true;
                }
            }
            for (int j = C-1; j >= 0; --j)
            {
                if (M[i][j] == '?')
                {
                    if (c)
                    {
                        M[i][j] = c;
                    }
                }
                else
                {
                    c = M[i][j];
                }
            }
        }

        for (int i = 1; i < R; ++i) {
            if (!G[i] && G[i - 1]) {
                M[i] = M[i - 1];
                G[i] = true;
            }
        }
        for (int i = R - 2; i >= 0; --i) {
            if (!G[i] && G[i + 1]) {
                M[i] = M[i + 1];
                G[i] = true;

            }
        }
        for (int i = 1; i < R; ++i) {
            if (!G[i] && G[i - 1]) {
                M[i] = M[i - 1];
                G[i] = true;

            }
        }

        out << "Case #" << (i + 1) << ":" << endl;
        for (int i = 0; i < R; ++i)
        {
            out << M[i] << endl;
        }

       /* for (int r = 0; r < R; ++r)
        {
            for (int c = 0; c < C; ++c)
            {
                for (int W = R; W >= 0; --W)
                {
                    for (int H = C; C >= 0; --H)
                    {
                        for (int dr = max(0, r - W + 1); dr < min(R, r + )
                        {

                        }
                    }
                }
            }
        }*/

    }

    return 0;
}

