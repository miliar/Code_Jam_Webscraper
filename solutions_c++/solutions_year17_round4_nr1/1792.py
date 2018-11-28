#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <iterator>
using namespace std;
int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A.out");
    int T;
    fin >> T;

    for (int t = 0; t < T; ++t)
    {
        int N, P;
        fin >> N >> P;

        int result = 0;

        std::vector<int> G;
        int one{};
        int two{};
        int three{};
        int four{};

        for (int i = 0; i < N; ++i)
        {
            int g;
            fin >> g;

            if (g % P == 0)
            {
                ++result;
            }
            else if (g % P == 1) ++one;
            else if (g % P == 2) ++two;
            else if (g % P == 3) ++three;
            else if (g % P == 4) ++four;
        }

        if (P == 2)
        {
            result += (one + 1) / 2;
        }
        else if (P == 3)
        {
            if (one >= two) {
                result += two;
                one -= two;
                result += (one + 2) / 3;
            }
            else
            {
                result += one;
                two -= one;
                result += (two + 2) / 3;
            }
        }
        else
        {
            result += two / 2;
            two = two % 2;

            if (one >= three)
            {
                result += three;
                one -= three;
                result = (one + 3 + two * 2) / 4;
            }
            else
            {
                result += one;
                three -= one;
                result += (three + 3 + two) / 4;
            }
        }

        fout << "Case #" << (t + 1) << ": " << result << endl;
    }

    return 0;
}