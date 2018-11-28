
/*
 * Michael V. Antosha
 * 2017
 * Michael.Antosha@gmail.com
 * http://mivael.in.ua
 */

#include <iostream>
using std::endl;
// using std::clog;
using std::istream;

#include <string>
using std::string;

#include <cassert>

static constexpr int MAX_SIZE = 25;

static constexpr char CH_BLANK = '?';

static bool assign_cake_row_if_occupied(string& S)
{
    static int source_for_copying[MAX_SIZE];

    const int C = S.size();
    for (int icol = 0;  icol < C;  ++icol)
    {
        int& icol_src = source_for_copying[icol];
        icol_src = icol;
        if (S[icol] == CH_BLANK)  ++icol_src;
    }

    int last_occup_ind = -1;
    for (int icol = C - 1;  icol >= 0;  --icol)
        if (source_for_copying[icol] == icol)  { last_occup_ind = icol;  break; }

    if (last_occup_ind < 0)  return false;

    for (int icol = last_occup_ind - 1;  icol >= 0;  --icol)
    {
        const int& icol_src = source_for_copying[icol];
        S[icol] = S[icol_src];
    }

    {
        const int& icol_src = source_for_copying[last_occup_ind];
        for (int icol = last_occup_ind + 1;  icol < C;  ++icol)
            S[icol] = S[icol_src];
    }

    return true;
}

int main(void)
{
    using std::cin;  using std::cout;
    std::ios_base::sync_with_stdio(false);  cin.tie(0);

    int T;  cin >> T;
    for (int tc = 1;  tc <= T;  ++tc)
    {
        int R, C;  cin >> R >> C;

        static string cake[MAX_SIZE];
        static int source_for_copying[MAX_SIZE];
        for (int irow = 0;  irow < R;  ++irow)
        {
            string& S = cake[irow];  cin >> S;
            assert((int)S.size() == C);

            int& irow_src = source_for_copying[irow];
            irow_src = irow;
            if (!assign_cake_row_if_occupied(S))
                ++irow_src;
        }

        int last_occup_ind = -1;
        for (int irow = R - 1;  irow >= 0;  --irow)
            if (source_for_copying[irow] == irow)  { last_occup_ind = irow;  break; }
        assert(last_occup_ind >= 0);

        for (int irow = last_occup_ind - 1;  irow >= 0;  --irow)
        {
            const int& irow_src = source_for_copying[irow];
            cake[irow] = cake[irow_src];
        }

        {
            const int& irow_src = source_for_copying[last_occup_ind];
            for (int irow = last_occup_ind + 1;  irow < R;  ++irow)
                cake[irow] = cake[irow_src];
        }

        cout << "Case #" << tc << ":\n";
        for (int irow = 0;  irow < R;  ++irow)  cout << cake[irow] << '\n';
        cout.flush();
    }
    return 0;
}
