
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

static constexpr char CH_BLANK = '-';
static constexpr char CH_HAPPY = '+';

static int minflips(const string& S, const int K)
{
    int first_blank = S.size();
    int last_blank = -1;
    for (int ii = 0;  ii < (int)S.size();  ++ii)
    {
        const char& ch = S[ii];
        if (ch == CH_BLANK)  last_blank = ii;
        if (ch == CH_BLANK  &&  first_blank > ii)  first_blank = ii;
    }

    string work = S;
    int flips = 0;
    while (first_blank <= last_blank)
    {
        if (last_blank - first_blank < K - 1)  return -1;

        ++flips;

        // Update work[] and first_blank.
        {
            bool frozen = false;
            const int end = first_blank + K;
            for (int pos = first_blank;  pos < end;  ++pos)
            {
                char& ch = work[pos];
                ch = (ch == CH_BLANK ? CH_HAPPY : CH_BLANK);

                if (!frozen  &&  ch == CH_HAPPY)  ++first_blank;
                if (ch == CH_BLANK)  frozen = true;
            }

            while (first_blank <= last_blank  &&  work[first_blank] == CH_HAPPY)
                ++first_blank;
        }

    }  // try another flip

    return flips;
}

int main(void)
{
    using std::cin;  using std::cout;
    std::ios_base::sync_with_stdio(false);  cin.tie(0);

    int T;  cin >> T;
    for (int tc = 1;  tc <= T;  ++tc)
    {
        string S;  int K;  cin >> S >> K;
        cout << "Case #" << tc << ": ";

        const int res = minflips(S, K);
        if (res < 0)  cout << "IMPOSSIBLE";
        else          cout << res;

        cout << '\n';
    }
    cout.flush();
    return 0;
}
